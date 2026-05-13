from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sort magical artifacts by power level (descending)."""
    try:
        return sorted(
            artifacts, key=lambda x: x['power'], reverse=True
        )
    except Exception:
        return None


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filter mages by minimum power level."""
    try:
        return list(
            filter(lambda x: x['power'] >= min_power, mages)
        )
    except Exception:
        return None


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spell names with decorative prefix and suffix."""
    try:
        return list(map(lambda x: "* " + x + " *", spells))
    except Exception:
        return None


def mage_stats(mages: List[Dict]) -> Dict:
    """Calculate power statistics for a list of mages."""
    try:
        powers = [m['power'] for m in mages]
        avg = sum(powers) / len(powers)

        return {
            'max_power': max(powers),
            'min_power': min(powers),
            'avg_power': avg
        }
    except Exception:
        return None


def main() -> None:

    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 83, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 70, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Casey', 'power': 50, 'element': 'fire'},
        {'name': 'Jordan', 'power': 66, 'element': 'light'},
        {'name': 'Sage', 'power': 80, 'element': 'wind'},
        {'name': 'Nova', 'power': 66, 'element': 'wind'},
        {'name': 'Ash', 'power': 68, 'element': 'fire'}
    ]
    spells = ['fireball', 'heal', 'shield']

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if sorted_artifacts and len(sorted_artifacts) > 1:
        first, second = sorted_artifacts[:2]
        print(
            f"{first['name']} ({first['power']} power) "
            f"comes before {second['name']} "
            f"({second['power']} power)"
        )
    else:
        print("Not enough artifacts to compare.")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    if transformed:
        print(" ".join(transformed))

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 66)
    if filtered_mages:
        formatted = ", ".join(
            f"{mage['name']} ({mage['power']})"
            for mage in filtered_mages
        )
        print(f"Mages with 66+ power: {formatted}")
    else:
        print("No mages meet the power threshold.")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    if stats:
        print(
            f"Mage stats: max {stats['max_power']}, "
            f"min {stats['min_power']}, "
            f"avg {stats['avg_power']:.1f}"
        )

    print()


if __name__ == "__main__":
    main()
