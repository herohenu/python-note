
cookies = "RK=E2F6RJyeRH; pgv_pvi=2789294080; pac_uid=111;  eas_sid=i1G5E0s2l5k9F9s446e1y1i3h5; pgv_pvid=9969283736; ptcz=582ccc92144882dc16d99d1b4976c4bba5e68be3175106a07c01c99acce998c1; pt2gguin=o0860884978; "
cookArr = cookies.split(";")
print cookArr
result = {}
for cook in cookArr:
    elem = cook.split("=")
    if len(elem ) == 2 :
        key = elem[0].strip()
        val = elem[1].strip()
        result[key] = val

print result
