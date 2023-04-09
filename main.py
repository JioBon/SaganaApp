from fastapi import FastAPI
from pydantic import BaseModel
from Crop import Crop
import reco

app = FastAPI()

# Onion
onion_stress = ["Botrytis leaf blight", "Downy Mildew", "Armyworm", "Leaf Miner"]
onion_stressDesc = [ 
    """Botrytis leaf blight, sometimes also referred to as Botrytis leaf spot, occurs on onions. 
    White, sunken spots on leaves are usually the first sign of infection. Spots are small, oval-shaped, and range from 0.06 to 0.25 inch (0.5–6 mm) long. 
    They sometimes have a light-green halo and may appear water-soaked. The epidermis around the spots may be silvery. 
    When numerous spots are present, leaf tips die back, and whole leaves may eventually die.""".strip(),
    """
    At the field level, symptoms of downy mildew are first noticed as circular clumps of yellowed plants that are a few to many feet in diameter. 
    As the disease progresses, the yellowing patterns often enlarge in the direction of prevailing winds.
    On individual plants, leaf tissue becomes pale green, then tan to brown or yellow, and finally collapses. Lesions may exhibit a violet-to-purple color. 
    When leaves are wet, or when humidity is very high, signs of Peronospora destructor are visible on the surface of older leaves as fine, furry, grayish-white growths. 
    These growths may later turn purple or brown as a result of a secondary infection of the lesion by other fungi, 
    such as those that cause PURPLE BLOTCH AND STEMPYLIUM LEAF BLIGHT, as these fungi can produce purple pigmentation and dark spores.
    """.replace('\n', ""),
    """

    """.replace('\n', ""),
    """
    Adults have yellow heads, knees, sides of abdomens; otherwise mostly dark gray, just over 1/10 inch long.
    Pupae are red-brown, slightly longer than adults.
    Larvae are white to yellow, up to about 1/3 inch long.
    Eggs are white, about 1/50 inch long, found on leaves.
    Adult feeding holes found in rows, with milky white sap coming out.
    """.replace('\n', "")
    ]
onion_stressSoln = [
    ["apply appropriate fungicide sprays".replace('\n', "")],
    ["""
    Spray at the first sign of the disease. After the first spray, scout fields and make subsequent applications when weather conditions are favorable for the disease. 
    Rotate with fungicides from different mode-of-action groups to reduce the risk of fungicide resistance development. 
    Fungicides may be applied on a 7-day schedule (only as consistent with the label), if necessary. 
    For all fungicides, thorough coverage of foliage is important in the control of downy mildew. 
    apply appropriate foliar fungicides taking care to apply thoroughly to waxy leaves. 
    Chlorothalonil and mancozeb are the main protectant fungicides for downy mildew.
    """.replace('\n', "")],
    ["".replace('\n', "")],
    ["""
    Pyrethrin This organic pesticide will kill leaf miners as they leave the egg and enter the leaf. 
    Since they have to chew into the leaf, they ingest the poison with the leaf and die. 
    However, pyrethrin also kills good insects such as bee and leaf miner preditors. 
    Use to spot treat concentrations of leaf miners rather than blanket the whole garden with it. 
    Be sure you get it on the bottom side of the leaf.
    """.replace('\n', "")]
]
for i in range(len(onion_stressSoln)):
    temp_list = []
    for j in range(len(onion_stressSoln[i])):
        temp_list = {"id": j, "Solution": onion_stressSoln[i][j]}
    onion_stressSoln[i] = temp_list
onion_data = Crop("Onion", "Allium cepa", onion_stress,  onion_stressDesc, onion_stressSoln)

## Corn
for i in range(len(reco.corn_stressSoln)):
    temp_list = []
    for j in range(len(reco.corn_stressSoln[i])):
        temp_list = {"id": j, "Solution": reco.corn_stressSoln[i][j]}
    reco.corn_stressSoln[i] = temp_list
corn_data = Crop("Corn", "Zea mays", reco.corn_stress, reco.corn_stressDesc, reco.corn_stressSoln)

## Eggplant
for i in range(len(reco.eggplant_stressSoln)):
    temp_list = []
    for j in range(len(reco.eggplant_stressSoln[i])):
        temp_list = {"id": j, "Solution": reco.eggplant_stressSoln[i][j]}
    reco.eggplant_stressSoln[i] = temp_list
eggplant_data = Crop("Eggplant", "Solanum melongena", reco.eggplant_stress, reco.eggplant_stressDesc, reco.eggplant_stressSoln)

## Tomato
for i in range(len(reco.tomato_stressSoln)):
    temp_list = []
    for j in range(len(reco.tomato_stressSoln[i])):
        temp_list = {"id": j, "Solution": reco.tomato_stressSoln[i][j]}
    reco.tomato_stressSoln[i] = temp_list
tomato_data = Crop("Tomato", "Solanum lycopersicum", reco.tomato_stress, reco.tomato_stressDesc, reco.tomato_stressSoln)

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Welcome to SaganaAPI!"}


@app.get("/{crop}")
async def get_Crop(crop: str):
    to_return = []
    if crop == "Onion":
        for i in range(len(onion_data.stress_dict)):
            to_return.append({"id": i, "stress": onion_data.stress_dict[i]})
        return to_return
    elif crop == "Corn":
        for i in range(len(corn_data.stress_dict)):
            to_return.append({"id": i, "stress": corn_data.stress_dict[i]})
        return to_return
    elif crop == "Eggplant":
        for i in range(len(eggplant_data.stress_dict)):
            to_return.append({"id": i, "stress": eggplant_data.stress_dict[i]})
        return to_return
    elif crop == "Tomato":
        for i in range(len(tomato_data.stress_dict)):
            to_return.append({"id": i, "stress": tomato_data.stress_dict[i]})
        return to_return
    else:
        return {"message": f"{crop} no on the list"}
    
@app.get("/allStress")
async def get_All():
    to_return = []
    for i in range(len(corn_data.stress_dict)):
        to_return.append({"id": i, "stress": corn_data.stress_dict[i]})
    for i in range(len(onion_data.stress_dict)):
        to_return.append({"id": i, "stress": onion_data.stress_dict[i]})
    for i in range(len(eggplant_data.stress_dict)):
        to_return.append({"id": i, "stress": eggplant_data.stress_dict[i]})
    for i in range(len(tomato_data.stress_dict)):
        to_return.append({"id": i, "stress": tomato_data.stress_dict[i]})
    return to_return
    
    
        

@app.get("/Onion/{stress}")
async def get_Onion(stress: str):
    for i in onion_data.stress_dict:
        if i['Stress'] == stress:
            return i
    else:
        return {"message": "Stress not found"}
    
@app.get("/Corn/{stress}")
async def get_Corn(stress: str):
    for i in corn_data.stress_dict:
        if i['Stress'] == stress:
            return i
    else:
        return {"message": "Stress not found"}
    
@app.get("/Eggplant/{stress}")
async def get_Eggplant(stress: str):
    for i in eggplant_data.stress_dict:
        if i['Stress'] == stress:
            return i
    else:
        return {"message": "Stress not found"}
    
@app.get("/Tomato/{stress}")
async def get_Tomato(stress: str):
    for i in tomato_data.stress_dict:
        if i['Stress'] == stress:
            return i
    else:
        return {"message": "Stress not found"}


# @app.post("/path")
# async def demo_post(inp: Msg):
#     return {"message": inp.msg.upper()}


# @app.get("/path/{path_id}")
# async def demo_get_path_id(path_id: int):
#     return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}