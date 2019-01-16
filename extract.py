# coding: utf-8
import os

import pandas as pd


def extract_data(filename,
                 sheet=0,
                 key="学号",
                 ps="平时成绩",
                 qz="期中成绩",
                 qm="期末成绩",
                 zp="总评成绩"):
    def extract_record(record):
        returns = {}
        if ps is not None and ps in record:
            returns["ps"] = record[ps]
        if qz is not None and qz in record:
            returns["qz"] = record[qz]
        if qm is not None and qm in record:
            returns["qm"] = record[qm]
        if zp is not None and zp in record:
            returns["zp"] = record[zp]
        return [record[key], returns]

    df = pd.read_excel(filename, sheet_name=sheet)
    export_list = list(df.apply(extract_record, axis=1))
    export_dict = dict(export_list)
    return str(export_list)


def get_prompt_msg(prompt, default=None):
    if default is not None:
        return "%s（默认为 %s ）: " % (prompt, default)
    return "%s: " % prompt


def get_input(prompt="请输入", validate=None, process=None, default=None):
    inp = input(get_prompt_msg(prompt, default))
    if validate is not None:
        msg = validate(inp)
        while msg is not None:
            inp = input(get_prompt_msg(prompt, default))
            msg = validate(inp)

    if process:
        return process(inp)
    return inp


def validate_file(filename):
    if os.path.exists(filename):
        return
    return "文件 `%s` 不存在！请重新输入"


if __name__ == "__main__":
    filename = get_input("请输入文件名", validate_file)
    sheet = get_input("请输入工作簿序号 ( 从 0 开始计数 )", default=0, process=int)
    key = get_input("请输入学号列的列名", default="学号")
    ps = get_input("请输入平时成绩的列名", default=None)
    qz = get_input("请输入期中成绩的列名", default=None)
    qm = get_input("请输入期末成绩的列名", default=None)
    zp = get_input("请输入总评成绩的列名", default=None)
    data = extract_data(filename, sheet, key, value)
    with open("paste_me_in_browser_console.js") as f:
        script = f.read()
    with open("%s_%s" % (filename, sheet), "w") as f:
        f.write(script[:7] + data + script[9:])
