import sys


def parse_args(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(':')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, raw_qty = parts[0], parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(raw_qty)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory.update({name: qty})
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_args(sys.argv[1:])
    if not inventory:
        print("Inventory is empty ;)")
        return

    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for name in inventory.keys():
        pct = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {pct}%")

    most = items[0]
    least = items[0]
    for name in inventory.keys():
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
