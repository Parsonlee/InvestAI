import re


def get_fullcode(code: str) -> str:
    if (
        code.startswith("00")
        or code.startswith("30")
        or code.startswith("15")
        or code.startswith("16")
    ):
        return f"sz{code}"
    elif code.startswith("60") or code.startswith("51"):
        return f"sh{code}"
    else:
        return code


def extract_code(fullcode: str) -> str:
    """
    基于正则提取基础股票6位数代码
    """
    pattern = r"^(sh|sz)?(\d{6})$"
    match = re.match(pattern, fullcode)
    if match:
        return match.group(2)
    return fullcode