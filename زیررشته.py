

#in code tavasote Amir Hossein Shirazi baratye tamrine shomare 19 pythone moqadamati neveshte shode ast




def test_abyaba(st):
    ab_pos = st.find('AB')
    ba_pos = st.find('BA')
    if ab_pos != -1 and ba_pos != -1:
        if st.find('BA', ab_pos + 2) != -1:
            print("YES")
        elif st.find('AB', ba_pos + 2) != -1:
            print('YES')
        else:
            print("NO")
    else:
        print('NO')
vorodi = input()
natije = test_abyaba(vorodi)
