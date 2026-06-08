import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    arg_list: list[int] = []
    i = 1
    while i < len(sys.argv):
        try:
            arg_val = int(sys.argv[i])
            arg_list.append(arg_val)
        except (Exception):
            print(f"Invalid parameter: '{sys.argv[i]}'")
        finally:
            i += 1
    if len(arg_list) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    print(f"Total players: {len(arg_list)}")
    print(f"Total score: {sum(arg_list)}")
    print(f"Average score: {sum(arg_list) / len(arg_list)}")
    print(f"High score: {max(arg_list)}")
    print(f"Low score: {min(arg_list)}")
    print(f"Score range: {max(arg_list) - min(arg_list)}")


if __name__ == "__main__":
    main()
