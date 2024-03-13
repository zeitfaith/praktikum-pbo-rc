import random

class Person:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child(Person):
    def __init__(self, father, mother):
        super().__init__(None)
        self.father_blood_type = father.blood_type
        self.mother_blood_type = mother.blood_type
        self.determine_child_blood_type()

    def determine_child_blood_type(self):
        father_alleles = [allele for allele in self.father_blood_type]
        mother_alleles = [allele for allele in self.mother_blood_type]

        random_father_allele = random.choice(father_alleles)
        random_mother_allele = random.choice(mother_alleles)

        child_alleles = [random_father_allele, random_mother_allele]
        child_alleles.sort()  # Sort alleles to determine blood type

        if random_father_allele == random_mother_allele:  # Homozygous
            child_blood_type = random_father_allele
        else:  # Heterozygous
            child_blood_type = ''.join(child_alleles)

        print("Goldar Anak:", child_blood_type)
        print("Alel Anak:", child_alleles)

# Input golongan darah Ayah
father_blood_type = input("Masukkan golongan darah Ayah: ")

# Input golongan darah Ibu
mother_blood_type = input("Masukkan golongan darah Ibu: ")

# Create Father, Mother, and Child objects
father = Person(father_blood_type)
mother = Person(mother_blood_type)
child = Child(father, mother)
