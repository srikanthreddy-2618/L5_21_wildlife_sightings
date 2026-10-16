"""Record and summarize wildlife sightings for a sanctuary."""

import hashlib
import sqlite3
from typing import Optional


def create_connection() -> sqlite3.Connection:
    """Create an in-memory database for the sightings demonstration."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE sightings (
            id INTEGER PRIMARY KEY,
            species TEXT NOT NULL,
            zone TEXT NOT NULL,
            count INTEGER NOT NULL CHECK (count >= 0)
        )
        """
    )
    return connection


def log_sighting(
    connection: sqlite3.Connection,
    species: str,
    zone: str,
    count: int,
    extras: Optional[dict[str, int]] = None,
) -> dict[str, int]:
    """Record one sighting and update the running species totals."""
    if not species.strip():
        raise ValueError("Species must not be empty.")
    if not zone.strip():
        raise ValueError("Zone must not be empty.")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer.")

    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count),
    )
    if extras is None:
        extras = {}
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer: str) -> str:
    """Return a short, deterministic identifier for display purposes.

    This hash is not intended for authentication or other
    security-sensitive use.
    """
    return hashlib.sha256(observer.encode("utf-8")).hexdigest()[:6]


def zone_summary(connection: sqlite3.Connection, zone: str) -> int:
    """Return the total number of animals recorded in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?",
        (zone,),
    ).fetchone()
    return row[0] if row and row[0] is not None else 0


def rarest_species(connection: sqlite3.Connection) -> Optional[str]:
    """Return the species with the smallest total count, or None if empty."""
    row = connection.execute(
        """
        SELECT species, SUM(count) AS total
        FROM sightings
        GROUP BY species
        ORDER BY total ASC, species ASC
        LIMIT 1
        """
    ).fetchone()
    return row[0] if row else None


def main() -> None:
    """Run a small demonstration of the wildlife sightings log."""
    connection = create_connection()
    try:
        totals = log_sighting(connection, "Leopard", "North", 1)
        log_sighting(connection, "Chital", "North", 24, totals)
        log_sighting(connection, "Hornbill", "East", 3, totals)

        if len(totals) != 3:
            raise RuntimeError("Expected totals for three species.")

        print(
            observer_id("Arun"),
            zone_summary(connection, "North"),
            rarest_species(connection),
        )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
