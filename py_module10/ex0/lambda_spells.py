def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    ttl_power = sum(map(lambda mage: mage["power"], mages))
    avg_power = round(ttl_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "artifact"},
        {"name": "Crystal Orb", "power": 85, "type": "artifact"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    try:
        print(f"{sorted_artifacts[0]['name']} "
              f"({sorted_artifacts[0]['power']} power)"
              f" comes before {sorted_artifacts[1]['name']} "
              f"({sorted_artifacts[1]['power']} power)")
    except Exception as e:
        print(e)

    print("\nTesting power filtering...")
    try:
        filtered_artifacts = power_filter(artifacts, 90)
        print(filtered_artifacts)
        filtered_artifacts_1 = power_filter(artifacts, 80)
        print(filtered_artifacts_1)
    except Exception as e:
        print(e)

    print("\nTesting spell transformer...")
    try:
        transformed = spell_transformer(["fireball", "heal", "shield"])
        for x in transformed:
            print(f"{x}", end=" ")
        print()
    except Exception as e:
        print(e)

    print("\nTesting mages stats...")
    try:
        stats = mage_stats(artifacts)
        print(f"Max power: {stats['max_power']}")
        print(f"Min power: {stats['min_power']}")
        print(f"Avg power: {stats['avg_power']}")
    except Exception as e:
        print(e)
