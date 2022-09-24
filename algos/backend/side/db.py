from typing import List


def solution(queries):
    db = {}
    result: List[str] = []
    for query in queries:
        operation = query[0]
        key = query[1] + "_" + query[2]
        if operation == "SET":
            result.append("")
            val = query[3]
            db[key] = val
        if operation == "GET":
            result.append(db.get(key, ""))
        if operation == "COMPARE_AND_SET":
            execpted_val = query[3]
            change_to = query[4]
            exists_val = db.get(key, "")
            if execpted_val == exists_val:
                result.append("true")
                db[key] = change_to
            else:
                result.append("false")
        if operation == "SCAN":
            scan_key = key.split("_")[0]
            suffix = key.split("_")[1]
            txts = []
            for x in db:
                key_db = x.split("_")[0]
                field_db = x.split("_")[1]
                if key_db == scan_key and field_db.startswith(suffix):
                    if db[x] == "":
                        txts.append("")
                    else:
                        txts.append(f"{field_db}({db[x]})")

            result.append(", ".join(list(sorted(txts, key=lambda txt: txt.split("(")[0]))))
    return result


if __name__ == '__main__':
    q = [["SET", "side", "side", "1"],
         ["SET", "side", "A", "0"],
         ["SCAN", "side", ""],
         ["COMPARE_AND_SET", "side", "side", "1", ""],
         ["COMPARE_AND_SET", "side", "A", "0", ""],
         ["COMPARE_AND_SET", "side", "A", "0", "7"],
         ["SET", "side", "A", "12"],
         ["SCAN", "side", ""],
         ["SCAN", "side", ""],
         ["GET", "side", "A"],
         ["SET", "A", "A", "18"],
         ["SCAN", "side", ""]]

    print(solution(q))
