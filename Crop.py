class Crop:
    def __init__(self, crop, sci_name, stresses, descriptions, solutions):
        self.crop = crop
        self.sci_name = sci_name
        self.stress_dict = []
        for i in range(len(stresses)):
            self.stress_dict.append({"Crop": self.crop, "Stress": stresses[i], "Description": descriptions[i], "Solutions": solutions[i]})

    def call_crop(self):
        return f"{self.crop}"
    
    def call_dict(self):
        return self.stress_dict