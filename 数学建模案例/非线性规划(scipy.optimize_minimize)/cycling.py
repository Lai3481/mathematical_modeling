# Tahan: base --> top 6 miles
# Ledang: b --> t 4 mil
# Jerai: b--> t 5 mil
# T --> L 3 mil
# L --> J 2 mil
# J --> T 5 mil

# D1: Tahan: base --> top 6 miles
# D5: T: b
# obj: max mil
# s.t. different peak per day

peak_from_b_to_t={'T':6,'L':4,'J':5}
Tahan_to_other={'L':3,'J':5}
Ledang_to_other={'T':3,'J':2}
Jerai_to_other={'L':2,'T':5}

route=[{'D1':'T'}]
mil=6

def cycling(mil):
    for i in range(1,5):
        if route[i-1][f'D{i}'] == 'T':
            route.append({f'D{i+1}':'J'})
            mil+=10
        elif route[i-1][f'D{i}'] == 'J':
            route.append({f'D{i+1}':'T'})
            mil+=11
        else:
            route.append({f'D{i+1}':'L'})
    return mil

if __name__=='__main__':
    mil_D5=cycling(mil)
    print(route,mil_D5)

