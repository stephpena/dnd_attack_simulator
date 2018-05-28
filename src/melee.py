import numpy as np

class Melee(object):
    ''' This class generates average attack damage sums based on given inputs

    Methods
    --------


    Attributes
    -----------

    '''

    def __init__(self):
        '''
        Parameters
        -----------

        '''

    def check_for_crit(atk_roll):
        if atk_roll == 20:
            is_crit = 1
        else:
            is_crit = 0
        return is_crit

    def roll_for_attack(atk_bonus):
        atk_roll = np.random.randint(1,high=21)
        atk_total = atk_roll + atk_bonus
        is_crit = check_for_crit(atk_roll)
        atk_output = np.array([atk_total,is_crit])
        return atk_output

    def roll_with_advantage(atk_bonus):
        atk_1 = roll_for_attack(atk_bonus)
        atk_2 = roll_for_attack(atk_bonus)
        atk_rolls = np.array([atk_1,atk_2])
        order_rolls = atk_rolls[atk_rolls[:,0].argsort()]
        adv_roll = order_rolls[-1]
        return adv_roll

    def get_attack_roll(atk_bonus,has_adv=bool(np.random.randint(2))):
        if has_adv == True:
            atk_output = roll_with_advantage(atk_bonus)
        else:
            atk_output = roll_for_attack(atk_bonus)
        return atk_output

    def get_atk_roll_outcome(atk_output):
        if atk_output[1] == 1:
            atk_outcome = 2
        elif atk_output[0] >= 15:
            atk_outcome = 1
        else:
            atk_outcome = 0
        return atk_outcome

    def check_for_sneak_attack(atk_output):
        if atk_output == 1:
            sneak_atk_output = np.random.randint(2)
        else:
            sneak_atk_output = atk_output
        return sneak_atk_output

    def roll_dice(num_rolls,num_sides):
        total = 0
        for i in range(num_rolls):
            total += np.random.randint(1,high=num_sides+1)
        return total

    def roll_for_damage(atk_output,atk_dice,sneak_atk_output,sneak_atk_dice,dmg_bonus=5):
        if atk_output == 2:
            atk_total = roll_dice(atk_dice[0]*2,atk_dice[1])
            sneak_total = roll_dice(sneak_atk_dice[0]*2,sneak_atk_dice[1])
            dmg_total = atk_total + sneak_total + dmg_bonus
        elif atk_output == 1 and sneak_atk_output == 1:
            atk_total = roll_dice(atk_dice[0],atk_dice[1])
            sneak_total = roll_dice(sneak_atk_dice[0],sneak_atk_dice[1])
            dmg_total = atk_total + sneak_total + dmg_bonus
        elif atk_output == 1 and sneak_atk_output == 0:
            atk_total = roll_dice(atk_dice[0],atk_dice[1])
            dmg_total = atk_total + dmg_bonus
        else:
            dmg_total = 0
        return dmg_total
