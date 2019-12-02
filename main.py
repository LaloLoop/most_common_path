def most_common_path(log):
    max_mcp = 0
    paths = {}
    mcps = {}

    for record in log:
        comps = record.split(",")

        user_id = comps[0]
        state = comps[1]

        if user_id not in paths:
            path = [state]
            paths[user_id] = path
        else:
            path = paths[user_id]
            if len(path) == 3:
                path = path[1:]
                path.append(state)
            else:
                path.append(state)

            paths[user_id] = path

            if len(path) == 3:
                path_str = "->".join(path)
                if path_str not in mcps:
                    mcps[path_str] = 1
                else:
                    mcps[path_str] += 1

                max_mcp = mcps[path_str]

    common_paths = []

    for common_path, count in mcps.items():
        if count == max_mcp:
            common_paths.append(common_path)

    if len(common_paths) > 1:
        return sorted(common_paths)
    else:
        return common_paths


def main():
    transactions = ["1,A", "1,B", "1,C", "1,D", "2,A", "2,B", "2,C", "2,D"]
    common_paths = most_common_path(transactions)

    if len(common_paths) == 0:
        print("Most common path not found!")

    else:
        for mcp in common_paths:
            print(mcp)

if __name__ == "__main__":
    main()