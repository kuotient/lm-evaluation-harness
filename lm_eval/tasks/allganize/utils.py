from datasets import Dataset
from sklearn.metrics import f1_score

def macro_f1_score(items):
    unzipped_list = list(zip(*items))
    y_true = unzipped_list[0]
    y_pred = unzipped_list[1]
    fscore = f1_score(y_true, y_pred, average='macro')
    return fscore

def fpb_doc_to_text(doc: dict) -> str:
    return f"""다음은 금융 뉴스에서 추출한 문장입니다. 해당 문장의 정서를 긍정, 중립, 부정 중 하나로 분류하세요. 문장: {doc["question"]} 정답:"""

def fiqasa_doc_to_text(doc: dict) -> str:
    return f"""다음은 금융 뉴스에서 추출한 문장입니다. 해당 문장의 정서를 긍정, 중립, 부정 중 하나로 분류하세요. 문장: {doc["question"]} 정답:"""