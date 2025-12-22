# Input: There are n men and n women
# • Each man has a preference list, so does each woman.
# • These lists have no ties.
# • Devise a system by which each of the n men and n women can end
# up getting married.
# • Different metrics possible:
# • Maximize the number of people who get their first match?
# • Maximize the average satisfaction?
# • Maximize the minimum satisfaction?

# • Can anything go wrong?

#bruteforse approach
from typing import Dict,List



def gale_shapley(m_pref:Dict,w_pref:Dict)->Dict:

    engagement:Dict=dict()
    single_men:List=[man for man in m_pref.keys()]
    womens_rank:Dict={
        w:{m:w_pref[w].index(m) for m in w_pref[w]} for w in w_pref
    }
    proposals:Dict={
        m:0 for  m in single_men
    }
    while single_men:
        man=single_men.pop(0)

        woman=m_pref[man][proposals[man]]
        proposals[man]+=1
        if woman not in engagement:
            engagement[woman]=man
        else:
            if womens_rank[woman][man] < womens_rank[woman][engagement[woman]]:
                dumped = engagement[woman]
                engagement[woman]=man 
                single_men.append(dumped)
                
            else:
                single_men.append(man)


    return engagement
