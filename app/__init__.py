"""Main application module for calculator REPL interface."""

import importlib
import logging
import logging.handlers
import os
import pkgutil
from dotenv import load_dotenv
from app.commands import Command, CommandHandler


class App:
    """Main application class handling initialization, 
    plugin loading, and REPL execution."""

    def __init__(self, start_repl=True):
        """Initialize application components and environment."""
        self.load_environment()
        self.setup_logging()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Application is Starting")
        self.command_handler = CommandHandler()
        self.load_plugins()
        self.logger.info("Application initialized")
        if start_repl:
            self.run_repl()

    def setup_logging(self):
        """Configure logging using environment variables."""
        log_level = self.settings.get('LOG_LEVEL', 'INFO').upper()
        log_output = self.settings.get('LOG_OUTPUT', './logs/app.log')

        os.makedirs(os.path.dirname(log_output), exist_ok=True)
        numeric_level = getattr(logging, log_level, logging.INFO)

        logging.basicConfig(
            level=numeric_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.handlers.RotatingFileHandler(
                    filename=log_output,
                    maxBytes=1048576,
                    backupCount=5
                )
            ]
        )

        # Test logger
        test_logger = logging.getLogger("setup_test")
        test_logger.info("Logging configured successfully with level %s at %s", log_level, log_output)

    def load_environment(self):
        """Load environment variables from .env file."""
        try:
            load_dotenv()
            self.settings = dict(os.environ)
            environment = self.get_environment_variable('ENVIRONMENT')
            print("Environment variables loaded successfully")
            print(f"Current environment: {environment}")
        except Exception as e:
            print(f"Failed to load environment variables: {str(e)}")
            raise

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Retrieve and validate environment variable."""
        value = self.settings.get(env_var, None)
        if not value:
            logging.warning("Environment variable %s not set", env_var)
        return value

    def load_plugins(self):
        """Discover and register plugin commands from plugins directory."""
        plugins_package = 'app.plugins'
        self.logger.info("Starting plugin loading process")
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            self.logger.error("Plugin directory %s not found", plugins_path)
            return

        for module_info in pkgutil.iter_modules([plugins_path]):
            self._process_plugin_module(plugins_package, module_info.name)

    def _process_plugin_module(self, plugins_package: str, plugin_name: str):
        try:
            plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
            self._register_commands_from_module(plugin_module)
        except Exception as error:
            self.logger.error("Error loading plugin %s: %s", plugin_name, str(error), exc_info=True)

    def _register_commands_from_module(self, plugin_module):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if not isinstance(item, type) or not issubclass(item, Command) or item == Command:
                continue
            command_instance = item() if item_name != 'MenuCommand' else item(self.command_handler)
            # Use lowercase class name without 'Command' suffix as command key
            command_key = item_name.replace('Command', '').lower()
            self.command_handler.register_command(command_key, command_instance)
            self.logger.info("Registered command: %s", command_key)

    def show_commands(self):
        """Print all available commands."""
        print("\nAvailable commands:")
        for cmd_name in sorted(self.command_handler.commands.keys()):
            print(f" - {cmd_name}")
        print("Type 'help' to show commands, 'exit' to quit.\n")

    def run_repl(self):
        """Run Read-Eval-Print Loop (REPL) interface for user interaction."""
        self.logger.info("Starting REPL interface")
        print("Welcome to Calculator!")
        self.show_commands()

        try:
            while True:
                try:
                    user_input = input(">>> ").strip()
                    self.logger.debug("User input: %s", user_input)

                    if not user_input:
                        continue

                    if user_input.lower() == "exit":
                        self.logger.info("Exit command received")
                        self.command_handler.execute_command("exit")
                        raise SystemExit("Exiting...")

                    if user_input.lower() in ['help', '?']:
                        self.show_commands()
                        continue

                    self._execute_command(user_input)

                except KeyboardInterrupt:
                    self.logger.info("Keyboard interrupt detected")
                    print("\nExiting...")
                    raise SystemExit("Exiting...")

        except Exception as e:
            self.logger.critical("REPL session failed", exc_info=True)
            raise e

    def _execute_command(self, user_input: str):
        parts = user_input.split()
        if not parts:
            return

        command_name, args = parts[0], parts[1:]
        command = self.command_handler.commands.get(command_name)
        if command and callable(command.execute):
            try:
                command.execute(*args) if args else command.execute()
            except TypeError as e:
                print(f"Error: {e}")
        else:
            print(f"No such command: {command_name}")


if __name__ == "__main__":
    App()
