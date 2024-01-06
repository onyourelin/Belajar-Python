def hitung_nilai_akhir(nilai_hadir,nilai_tugas,nilai_uts,nilai_uas):
    bobot_hadir = 0.15
    bobot_tugas = 0.25
    bobot_uts = 0.3
    bobot_uas = 0.3    
    nilai_akhir = bobot_hadir * nilai_hadir + bobot_tugas * nilai_tugas + bobot_uts * nilai_uts + bobot_uas * nilai_uas
    return nilai_akhir

def nilai_ke_grade(nilai_akhir):
    grade = 'E'
    if nilai_akhir >= 85:
        grade = 'A'
    elif nilai_akhir >= 70:
        grade = 'B'
    elif nilai_akhir >= 50:
        grade = 'C'
    elif nilai_akhir >= 40:
        grade = 'D'
    return grade

nilai_edward = hitung_nilai_akhir(80, 75, 90, 70);
grade_edward = nilai_ke_grade(nilai_edward)

nilai_bella = hitung_nilai_akhir(90, 95, 80, 80);
grade_bella = nilai_ke_grade(nilai_bella)

print('Nilai akhir Edward = {}, dengan grade= {}'.format(nilai_edward,grade_edward))
print('Nilai akhir Bella = {}, dengan grade= {}'.format(nilai_bella,grade_bella))