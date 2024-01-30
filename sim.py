import random
import statistics

# number of pulls
samples = 10000000
char_worst_case = 89
event_char_worst_case = 178
wep_worst_case = 77
event_wep_worst_case = 231

# gacha costs
pull_cost = 160  # primogem cost per pull
max_pack_cost = 99.99  # USD
top_up_packs = {0.99: 120, 4.99: 600, 14.99: 1960, 29.99: 3960, 49.99: 6560, 99.99: 12960}  # price to crystals
base_crystals = 8080

def event_sim(base_rate: float, rate_mod: float, event_chance: float,
              event_guarantee: int, soft_pity: int, hard_pity: int) -> dict:
    five_star_count = 0
    rate_up_count = 0
    five_star_pull_count = []
    event_pull_count = []
    current_rate = base_rate
    current_pity = 0  # pity for any 5 star
    event_pity = 0 # pity for event 5 star
    offrate_count = 0  # find a non event 5 star
    for x in range(samples):
        if current_pity >= soft_pity:  # change rates when in soft pity range
            current_rate += rate_mod

        if random.random() >= 1 - current_rate or current_pity == hard_pity:  # roll a 5 star
            if random.random() >= 1 - event_chance or offrate_count >= event_guarantee:  # roll an event 5 star
                rate_up_count += 1
                event_pull_count.append(event_pity)
                event_pity = 0
                offrate_count = 0
            else:   # roll a non event 5 star
                offrate_count += 1
            five_star_count += 1
            five_star_pull_count.append(current_pity)
            # reset pity and rates
            current_pity = 0
            current_rate = base_rate
        current_pity += 1
        event_pity += 1
    five_star_pull_count.sort()
    event_pull_count.sort()
    return {'event_five_star_count': rate_up_count,
            'all_five_star_count': five_star_count,
            'five_star_median': statistics.median(five_star_pull_count),
            'event_median': statistics.median(event_pull_count)}


def get_costs(counts: list):
    cost = max_pack_cost / (base_crystals / pull_cost)  # get cost of a pull in USD
    cost_list = []
    for c in counts:
        cost_list.append(format(cost * c, '.2f'))  # round 2 decimal places
    return cost_list


def main():
    # get avgs for event character banner
    base_rate = 0.006
    rate_mod = 0.06
    event_chance = 0.5
    event_guarantee = 1
    soft_pity = 74
    hard_pity = 90

    print(f'# of samples: {samples}')

    avgs = event_sim(base_rate, rate_mod, event_chance, event_guarantee, soft_pity, hard_pity)
    event_avg = int(samples / avgs['event_five_star_count'])
    total_avg = int(samples / avgs['all_five_star_count'])
    event_median = avgs['event_median']
    total_median = avgs['five_star_median']
    print(f'Average # of pulls for any 5* character: {total_avg}')
    print(f'Average # of pulls for event 5* character: {event_avg}')
    print(f'Median # of pulls for any 5* character: {total_median}')
    print(f'Median # of pulls for event 5* character: {event_median}')

    pull_counts = set([i for i in range(10, 181, 10)])  # get multiples of 10
    pull_counts.add(event_avg)
    pull_counts.add(total_avg)
    pull_counts.add(event_median)
    pull_counts.add(total_median)
    pull_counts.add(char_worst_case)
    pull_counts.add(event_char_worst_case)
    print(sorted(pull_counts))
    standard_cost_list = get_costs(sorted(pull_counts))  # price of pulls with standard top up
    print(standard_cost_list)

    # get avgs for event weapon banner
    base_rate = 0.007
    rate_mod =  0.07
    event_chance = 0.35
    event_guarantee = 2
    soft_pity = 63
    hard_pity = 80

    print(f'# of samples: {samples}')

    avgs = event_sim(base_rate, rate_mod, event_chance, event_guarantee, soft_pity, hard_pity)
    event_avg = int(samples / avgs['event_five_star_count'])
    total_avg = int(samples / avgs['all_five_star_count'])
    event_median = avgs['event_median']
    total_median = avgs['five_star_median']
    print(f'Average # of pulls for any 5* weapon: {total_avg}')
    print(f'Average # of pulls for event 5* weapon: {event_avg}')
    print(f'Median # of pulls for any 5* weapon: {total_median}')
    print(f'Median # of pulls for event 5* weapon: {event_median}')

    pull_counts = set([i for i in range(10, 241, 10)])  # get multiples of 10
    pull_counts.add(event_avg)
    pull_counts.add(total_avg)
    pull_counts.add(event_median)
    pull_counts.add(total_median)
    pull_counts.add(wep_worst_case)
    pull_counts.add(event_wep_worst_case)
    print(sorted(pull_counts))
    standard_cost_list = get_costs(sorted(pull_counts))  # price of pulls with standard top up
    print(standard_cost_list)
