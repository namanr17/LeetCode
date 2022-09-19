class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files_dict = defaultdict(list)
        
        for path in paths:
            files = path.split(' ')
            
            dir_ = files[0]
            for file in files[1:]:
                name, content = file.split('(')
                files_dict[content[:-1]].append(dir_ + '/' + name)
            
        return [i for i in files_dict.values() if len(i) > 1]