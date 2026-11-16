class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        global_hashmap={}
        for s in strs : 
            local_hashmap={}
            for c in s :
                local_hashmap[c]=local_hashmap.get(c,0)+1
            global_key = ";".join(f"{k}:{v}" for k, v in sorted(local_hashmap.items()))
            global_hashmap[global_key]=global_hashmap.get(global_key,[]) + [s]
        #print(local_hashmap)
        print(global_hashmap)
        return list(global_hashmap.values())