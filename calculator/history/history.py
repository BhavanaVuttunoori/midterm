"""Manages a history of mathematical operations."""

from typing import List, Optional
from calculator.calculation import OperationRecord


class OperationHistory:
    """
    Stores and manages a list of past OperationRecord instances.
    """

    _history: List[OperationRecord] = []  # Shared class-level history list

    @classmethod
    def add_record(cls, record: OperationRecord) -> None:
        """Add a new operation record to the history."""
        cls._history.append(record)

    @classmethod
    def get_all_records(cls) -> List[OperationRecord]:
        """Return all stored operation records."""
        return cls._history

    @classmethod
    def clear_records(cls) -> None:
        """Clear all stored operation records."""
        cls._history = []

    @classmethod
    def get_last_record(cls) -> Optional[OperationRecord]:
        """
        Get the most recent operation record.

        Returns:
            Optional[OperationRecord]: The last record, or None if history is empty.
        """
        if cls._history:
            return cls._history[-1]
        return None
