class Crop:
    def __init__(self, crop, sci_name, stresses, descriptions, solutions):
        self.crop = crop
        self.sci_name = sci_name
        self.stresses = stresses
        self.descriptions = descriptions
        self.solutions = solutions

        self.stress_dict = []
        for i in range(len(stresses)):
            self.stress_dict.append({"Crop": self.crop, "Scientific": self.sci_name, "Stress": self.stresses[i], "Description": self.descriptions[i], "Solutions": self.solutions[i]})

    def call_crop(self):
        return f"{self.crop}"
    
    def call_dict(self):
        return f"{self.stress_dict}"