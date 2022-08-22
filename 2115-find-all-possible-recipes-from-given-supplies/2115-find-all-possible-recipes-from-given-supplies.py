class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
            
        ret = []
        done = set(supplies)
        
        def canBeMade(i):
            made = False
            for item in ingredients[i]:
                if item not in done:
                    return False
                made = True
            if made:
                ret.append(recipes[i])
                done.add(recipes[i])
            return made
        
        made = True
        while(made):
            made = False
            for i in range(len(recipes)):
                if recipes[i] not in done:
                    made |= canBeMade(i)
        
        return ret