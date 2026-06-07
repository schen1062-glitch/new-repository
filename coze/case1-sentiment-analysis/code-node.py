async def main(args):
    user_input = args.params.get('user_input', '')

    # 定义情绪关键词
    anger_keywords = ['差劲', '烂', '垃圾', '坑', '投诉', '不会再买', '骗子', '太差了', '恶心', '愤怒', '退货', '再也不会', '最后一次']
    disappointment_keywords = ['失望', '没想到', '以为', '原来', '太慢', '破损', '少了', '错了', '没达到', '一般', '还行吧', '凑合']
    calm_keywords = ['建议', '希望', '如果能', '虽然但是', '还行', '总体', '不错但是']

    # 情绪提取逻辑
    extracted_emotion = None
    for word in anger_keywords:
        if word in user_input:
            extracted_emotion = '愤怒'
            break

    if not extracted_emotion:
        for word in disappointment_keywords:
            if word in user_input:
                extracted_emotion = '失望'
                break

    if not extracted_emotion:
        for word in calm_keywords:
            if word in user_input:
                extracted_emotion = '平静'
                break

    if not extracted_emotion:
        extracted_emotion = '失望'  # 默认情绪

    return {
        "extracted_emotion": extracted_emotion,
        "original_text": user_input
    }
