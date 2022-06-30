class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        st = []
        for ch in s:
            if ch == "#":
                if ss:
                    ss.pop()
            else:
                ss.append(ch)
        
        for ch in t:
            if ch == "#":
                if st:
                    st.pop()
            else:
                st.append(ch)
               
        return ss == st
        
                
        
        
        
        