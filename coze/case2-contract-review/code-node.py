import re

async def main(args):
    contract_text = args.params.get('contract_text', '')

    # 按"第X条"或"第X款"拆分条款
    # 支持中文数字和阿拉伯数字
    pattern = r'(?=第[一二三四五六七八九十\d]+[条|款])'
    clauses = re.split(pattern, contract_text)

    # 过滤空字符串和过短片段
    clauses = [c.strip() for c in clauses if len(c.strip()) > 10]

    # 如果没有成功拆分，整体作为一条
    if not clauses:
        clauses = [contract_text]

    # 返回拆分后的条款列表
    result = []
    for i, clause in enumerate(clauses):
        result.append({
            "clause_index": i + 1,
            "clause_content": clause,
            "total_clauses": len(clauses)
        })

    return {
        "clauses": result,
        "total_count": len(clauses)
    }
