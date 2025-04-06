from config import *
from analytics import Research

def all_together():
    res = Research(path_to_file)
    num_observations = len(res.data)
    heads_tails = res.calculation.counts()
    heads = heads_tails[1]
    tails = heads_tails[0]
    heads_fract, tail_fract = res.calculation.fractions(heads_tails)
    predict = res.calculation.predict_random(num_forecast)
    heads_predict = 0
    tails_predict = 0
    for i in predict:
        if i[0] == 0:
            tails_predict += 1
        else:
            heads_predict += 1
    text_report = template.format(num_observations, tails, heads,
                                  tail_fract, heads_fract, num_forecast,
                                  tails_predict, heads_predict)
    res.calculation.save_file(text_report, output_file)

if __name__ == '__main__':
    all_together()