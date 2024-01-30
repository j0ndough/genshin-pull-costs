# genshin-pull-costs

A quick sim to calculate the average and median of getting 5*'s in Genshin Impact. Also calculcates the cost at
certain pull counts.

Might turn this into an interactive sliding graph later.

## Gacha Rates

Source: https://www.hoyolab.com/article/497840

Event Character Wish TL;DR:

- Pulls 1-73 have a **0.6% chance** (base chance) to get a 5*.
- Starting with the 74th pull, your chance to get a 5* increases by **6 percent each time**.
This means the 74th pull will have 6.6% chance to get a 5*, the 75th pull will have a 12.6% chance, and so on.
- Because of this, it is near impossible to hit "true" pity at 90 pulls.
The expected worst case to get ANY 5* character is **89 pulls**.
- 50/50 guarantee: If the 5* character you get is not the event character, your next 5* is guaranteed to be the
event 5* character. Expected worst case for 5* event character: **178 pulls**. Theoretical worst case: **180 pulls**.

Event Weapon Wish TL;DR:
- Pulls 1-62 have a **0.7% chance** (base chance) to get a 5*.
- Starting with the 63rd pull, your chance to get a 5* increases by **7 percent each time**.
This means the 63th pull will have 7.7% chance to get a 5*, the 75th pull will have a 14.7% chance, and so on.
- Because of this, it is near impossible to hit "true" pity at 80 pulls.
The expected worst case to get ANY 5* weapon is **77 pulls**.
- Epitomized path: You have the option of selecting the rate-up 5* weapon you want. If the 5* you get on the
banner is not that weapon, gain a pity point. At 2 pity points, your next 5* is guaranteed to be that weapon.
Expected worst case for desired rate-up 5* weapon: **231 pulls**. Theoretical worst case: **240 pulls**.

## Cost Breakdown Tables

This breakdown assumes the player has no pulls of their own, from any source
(such as Genesis Crystals, Primogems, and Fates).

For cost in USD, the $100 Genesis Crystal pack (no top-up bonus) is used for calculation,
as it is the cheapest for pulls (~$1.98 USD/pull).

**Event Character Cost:**
| # of Pulls                                | Cost in USD |
|-------------------------------------------|-------------|
| 1                                         | $1.98       |
| 10                                        | $19.80      |
| 20                                        | $39.60      |
| 30                                        | $59.40      |
| 40                                        | $79.20      |
| 50                                        | $99.00      |
| 60                                        | $118.80     |
| 62 (average # of pulls for ANY 5*)        | $122.76     |
| 70                                        | $138.60     |
| 76 (median # of pulls for ANY 5*)         | $150.48     |
| 80 (median # of pulls for event 5*)       | $158.40     |
| 89 (expected worst case for ANY 5*)       | $176.22     |
| 90 (theoretical worst case for ANY 5*)    | $178.20     |
| 93 (average # of pulls for event 5*)      | $182.16     |
| 100                                       | $198.00     |
| 110                                       | $217.80     |
| 120                                       | $237.60     |
| 130                                       | $257.40     |
| 140                                       | $277.20     |
| 150                                       | $297.00     |
| 160                                       | $316.80     |
| 170                                       | $336.60     |
| 178 (expected worst case for event 5*)    | $352.44     |
| 180 (theoretical worst case for event 5*) | $356.40     |

**Event Weapon Cost:**
| # of Pulls                                   | Cost in USD |
|----------------------------------------------|-------------|
| 1                                            | $1.98       |
| 10                                           | $19.80      |
| 20                                           | $39.60      |
| 30                                           | $59.40      |
| 40                                           | $79.20      |
| 50                                           | $99.00      |
| 53 (average # of pulls for ANY 5*)           | $104.94     |
| 60                                           | $118.80     |
| 65 (median # of pulls for ANY 5*)            | $128.70     |
| 70                                           | $138.60     |
| 77 (expected worst case for ANY 5*)          | $152.46     |
| 80 (theoretical worst case for ANY 5*)       | $158.40     |
| 90                                           | $178.20     |
| 100                                          | $198.00     |
| 110 (average/median # of pulls for event 5*) | $217.80     |
| 120                                          | $237.60     |
| 130                                          | $257.40     |
| 140                                          | $277.20     |
| 150                                          | $297.00     |
| 160                                          | $316.80     |
| 170                                          | $336.60     |
| 180                                          | $356.40     |
| 190                                          | $376.20     |
| 200                                          | $396.00     |
| 210                                          | $415.80     |
| 220                                          | $435.60     |
| 230                                          | $455.40     |
| 231 (expected worst case for event 5*)       | $457.38     |
| 240 (theoretical worst case for event 5*)    | $475.20     |