# coding: utf-8
import os

import pandas as pd


def extract_data(filename, sheet=0, key="学号", value="期末成绩"):
    df = pd.read_excel(filename, sheet_name=sheet)
    export_list = list(df.apply(lambda x: [x[key], x[value]], axis=1))
    export_dict = dict(export_list)
    with open("%s_%s.txt" % (filename, sheet), "w") as f:
        f.write(str(export_list))


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
    value = get_input("请输入期末成绩的列名", default="期末成绩")
    extract_data(filename, sheet, key, value)
