from easynmt import EasyNMT
model = EasyNMT('mbart50_m2en')

#Translate several sentences to English
sentences = [
'腹主动脉左旁结节灶，增大的淋巴结？肝左叶小低密度灶。胆囊小结石，胆囊炎。左肾囊肿。左侧肾上腺稍粗。脐疝。请结合临床及其他相关检查，定期随诊对比变化。全子宫+附件切除术后。请结合临床及其他相关检查，随诊。左肺微小结节。左肺下叶条索影。深静脉置管中。请结合临床及其他相关检查，随诊。', 
'腹部主动脉左侧旁结节灶，存在增大的淋巴结？肝脏左叶发现小的低密度病灶。胆囊内有小型结石，同时伴有胆囊炎。左肾出现囊肿，左侧肾上腺稍显粗大。还存在脐疝。请结合临床病情及其他相关检查，定期随访以对比病情变化。', 
'胆囊切除术后。双肾囊肿。左侧肾上腺体部稍增粗。右半结肠壁局部增厚。请结合临床及其他相关检查，随诊。',
'胆囊小结石；脾大；脾静脉增宽，门静脉主干稍宽。请结合临床及其他相关检查，随诊。',
#'胃术后改变，术区渗出积液，较2023-02-08前片减少，吻合口壁略厚，网膜囊结构紊乱伴小淋巴结；少量腹腔积液；肝S6及S2段包膜下低密度灶；胆囊壁略厚；胰头饱满；两肾囊肿；请结合临床和其他检查，随访。附见少量心包积液；右侧少量胸腔积液伴两下肺膨胀不全；所示两肺斑片条索影。', 
'胰头密度欠均匀，胰管及胆总管置管中，肝内外胆管扩张积气；肝内低密度灶，部分拟囊肿，部分性质待定；胆囊炎；脾内低密度灶，脉管瘤可能；双肾囊肿。肝门部稍大淋巴结。请结合临床及其他相关检查，随诊。'
        ] #This is a spanish sentence
ret = model.translate(sentences, target_lang='en')

for i in range(len(sentences)):
    print()
    print(sentences[i])
    print(ret[i])
