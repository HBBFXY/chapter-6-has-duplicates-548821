def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数：lst - 任意列表
    返回：bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 利用集合元素唯一性，若列表转集合后长度变短，说明有重复
    return len(lst) != len(set(lst))

# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],  # 无重复
        [1, 2, 2],  # 有重复
        ["一个", "乙", "一个"],  # 字符串重复
        []  # 空列表
    ]

    # 测试每个用例，编写具体测试代码
    for idx, case in enumerate(test_cases, 1):
        result = has_duplicates(case)
        print(f"测试用例 {idx}：{case}，有重复元素：{result}")
