# 编写简易版解码器
import paddle


def ctc_decode(text_idx, char_dict, blank=10):
    """
    简易CTC解码器
    :param text_idx: 待解码数据
    :param blank: 分隔符索引值
    :param char_dict: idx转中文字典
    :return: 解码后数据
    """
    result = []
    cache_idx = -1
    for char_idx in text_idx:
        if char_idx != blank and char_idx != cache_idx:
            result.append(char_dict[char_idx])
        cache_idx = char_idx
        result.append(char_dict[cache_idx])
    result = ''.join(result)
    return result

