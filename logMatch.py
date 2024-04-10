import torch
import numpy as np
from transformers import BertTokenizer, BertModel, BertForMaskedLM
from sklearn.metrics.pairwise import euclidean_distances  # 欧氏距离
from sklearn.metrics.pairwise import cosine_similarity  # 余弦距离
import json
import pandas as pd

# 初始化BERT模型和分词器
model_class, tokenizer_class, pretrained_weights = (BertModel,BertTokenizer, 'chinese-bert-wwm-ext')
#                                                    模型             分词器            词汇表
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)  # 定义分词器
bert_model = model_class.from_pretrained(pretrained_weights)     # 定义模型
def similar_count(vec, vec2, model="cos"):
    '''
    计算距离
    :param vec: 句向量1
    :param vec2: 句向量2
    :param model: 用欧氏距离还是余弦距离
    :return: 返回的是两个向量的距离得分
    '''
    if model == "eu":
        return euclidean_distances([vec, vec2])[0][1]
    if model == "cos":
        return cosine_similarity([vec, vec2])[0][1]
    
def bert_vec(text):
        marked_text = "[CLS] " + text + " [SEP]"
        # print (marked_text)
        tokenized_text = tokenizer.tokenize(marked_text)
        
        # print (tokenized_text)
        indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
        # print(indexed_tokens)
        
        batch_tokenized = tokenizer.batch_encode_plus([text], padding=True, truncation=True, max_length=20)
       
        # print(batch_tokenized)
        input_ids = torch.tensor(batch_tokenized['input_ids'])
        attention_mask = torch.tensor(batch_tokenized['attention_mask'])
        bert_output = bert_model(input_ids, attention_mask=attention_mask)
        # print(bert_output[0].shape)
        bert_cls_hidden_state = bert_output[0][:,0,:]
        # print("48",bert_cls_hidden_state.shape) 
        return np.array(bert_cls_hidden_state[0].detach().numpy())


def match(sentences, keyword) ->tuple:
    keyword_vec = bert_vec(keyword)
    similarities_dict = {} # 创建空字典，用于存储相似度
    for sentence in sentences:
        if sentence.strip():  # 确保句子不只是空格
            vec = bert_vec(sentence)
            similarity = similar_count(vec, keyword_vec, model="cos")
            similarities_dict[sentence] = similarity


    sorted_similarity = sorted(similarities_dict.items(), key=lambda x: x[1], reverse=True)
    # item[0], ":", item[1]
    return sorted_similarity[0]

