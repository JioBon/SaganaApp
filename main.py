from fastapi import FastAPI, Query, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from Crop import Crop
import reco
import pandas as pd
import os
import sqlite3
import base64

app = FastAPI()



# @app.post("/signin/")
# async def check_user(First_name: str, Last_name: str, Username: str, Password: str,):
#     conn=sqlite3.connect("Userdatabase.db")
#     cursor=conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE First_name = ?, Last_name = ?, Password = ?, Username = ? ",(First_name,Last_name,Password,Username))
#     result.cursor.fetchone()
#     if result:
#         return print("Signed in") 
#     conn.close()
#     cursor.close()

# @app.get("/dictionary/")
# async def Dictiory():
#     conn=sqlite3.connect("Userdatabase.db")
#     cursor=conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     data = cursor.fetchone()
#     my_dict = {}
#     my_dict["Username"]=data[0]
#     my_dict["First_name"]=data[1]
#     my_dict["Last_name"]=data[2]
#     my_dict["Password"]=data[3]
#     cursor.close()
#     conn.close()
#     return my_dict


# # Onion
# onion_stress = ["Botrytis leaf blight", "Downy Mildew", "Armyworm", "Leaf Miners"]
# onion_stressDesc = [ 
#     """Botrytis leaf blight, sometimes also referred to as Botrytis leaf spot, occurs on onions. 
#     White, sunken spots on leaves are usually the first sign of infection. Spots are small, oval-shaped, and range from 0.06 to 0.25 inch (0.5–6 mm) long. 
#     They sometimes have a light-green halo and may appear water-soaked. The epidermis around the spots may be silvery. 
#     When numerous spots are present, leaf tips die back, and whole leaves may eventually die.""".strip(),
#     """
#     At the field level, symptoms of downy mildew are first noticed as circular clumps of yellowed plants that are a few to many feet in diameter. 
#     As the disease progresses, the yellowing patterns often enlarge in the direction of prevailing winds.
#     On individual plants, leaf tissue becomes pale green, then tan to brown or yellow, and finally collapses. Lesions may exhibit a violet-to-purple color. 
#     When leaves are wet, or when humidity is very high, signs of Peronospora destructor are visible on the surface of older leaves as fine, furry, grayish-white growths. 
#     These growths may later turn purple or brown as a result of a secondary infection of the lesion by other fungi, 
#     such as those that cause PURPLE BLOTCH AND STEMPYLIUM LEAF BLIGHT, as these fungi can produce purple pigmentation and dark spores.
#     """.replace('\n', ""),
#     """

#     """.replace('\n', ""),
#     """
#     Adults have yellow heads, knees, sides of abdomens; otherwise mostly dark gray, just over 1/10 inch long.
#     Pupae are red-brown, slightly longer than adults.
#     Larvae are white to yellow, up to about 1/3 inch long.
#     Eggs are white, about 1/50 inch long, found on leaves.
#     Adult feeding holes found in rows, with milky white sap coming out.
#     """.replace('\n', "")
#     ]
# onion_stressSoln = [
#     ["apply appropriate fungicide sprays".replace('\n', "")],
#     ["""
#     Spray at the first sign of the disease. After the first spray, scout fields and make subsequent applications when weather conditions are favorable for the disease. 
#     Rotate with fungicides from different mode-of-action groups to reduce the risk of fungicide resistance development. 
#     Fungicides may be applied on a 7-day schedule (only as consistent with the label), if necessary. 
#     For all fungicides, thorough coverage of foliage is important in the control of downy mildew. 
#     apply appropriate foliar fungicides taking care to apply thoroughly to waxy leaves. 
#     Chlorothalonil and mancozeb are the main protectant fungicides for downy mildew.
#     """.replace('\n', "")],
#     ["".replace('\n', "")],
#     ["""
#     Pyrethrin This organic pesticide will kill leaf miners as they leave the egg and enter the leaf. 
#     Since they have to chew into the leaf, they ingest the poison with the leaf and die. 
#     However, pyrethrin also kills good insects such as bee and leaf miner preditors. 
#     Use to spot treat concentrations of leaf miners rather than blanket the whole garden with it. 
#     Be sure you get it on the bottom side of the leaf.
#     """.replace('\n', "")]
# ]


# for i in range(len(onion_stressSoln)):
#     temp_list = []
#     for j in range(len(onion_stressSoln[i])):
#         temp_list = {"id": j, "Solution": onion_stressSoln[i][j]}
#     onion_stressSoln[i] = temp_list
# onion_data = Crop("Onion", "Allium cepa", onion_stress,  onion_stressDesc, onion_stressSoln)

# ## Corn
# for i in range(len(reco.corn_stressSoln)):
#     temp_list = []
#     for j in range(len(reco.corn_stressSoln[i])):
#         temp_list = {"id": j, "Solution": reco.corn_stressSoln[i][j]}
#     reco.corn_stressSoln[i] = temp_list
# corn_data = Crop("Corn", "Zea mays", reco.corn_stress, reco.corn_stressDesc, reco.corn_stressSoln)

# ## Eggplant
# for i in range(len(reco.eggplant_stressSoln)):
#     temp_list = []
#     for j in range(len(reco.eggplant_stressSoln[i])):
#         temp_list = {"id": j, "Solution": reco.eggplant_stressSoln[i][j]}
#     reco.eggplant_stressSoln[i] = temp_list
# eggplant_data = Crop("Eggplant", "Solanum melongena", reco.eggplant_stress, reco.eggplant_stressDesc, reco.eggplant_stressSoln)

# ## Tomato
# for i in range(len(reco.tomato_stressSoln)):
#     temp_list = []
#     for j in range(len(reco.tomato_stressSoln[i])):
#         temp_list = {"id": j, "Solution": reco.tomato_stressSoln[i][j]}
#     reco.tomato_stressSoln[i] = temp_list
# tomato_data = Crop("Tomato", "Solanum lycopersicum", reco.tomato_stress, reco.tomato_stressDesc, reco.tomato_stressSoln)

# Get Plant Data
plant_details_df = pd.read_csv(f"csv/plant_details.csv", header=0, names=None, encoding="utf8")
plant_details = plant_details_df.to_dict(orient="records")

# Get Stress Data
stress_details_df = pd.read_csv(f"csv/stress_details.csv", header=0, names=None, encoding='windows-1254')
stress_details_df = stress_details_df.fillna('')
stress_details = stress_details_df.to_dict(orient="records")

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
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

@app.post("/User_data/")
async def User_Data(First_name: str = Query(...), Last_name: str = Query(...), Username: str = Query(...), Password: str = Query(...)):
    conn=sqlite3.connect("Userdatabase.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Username = ?", (Username,))
    result = cursor.fetchall()
    print(result)
    if not result:
        cursor.execute("INSERT INTO users (Username, First_name, Last_name, Password) VALUES (?,?,?,?)", 
        (Username,First_name,Last_name,Password))
        conn.commit()
    else:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="User already exist. Please Try different Username")
    cursor.close()
    conn.close()

@app.get("/select_from_database/{Username}")
async def get_user_specificuser(Username: str):
    conn=sqlite3.connect("Userdatabase.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Username = ?",(Username,))
    result=cursor.fetchone()
    my_dict = {}
    my_dict["Username"]=result[0]
    my_dict["First_name"]=result[1]
    my_dict["Last_name"]=result[2]
    my_dict["Password"]=result[3]
    my_dict["Contact_no"]=result[4]
    my_dict["Profile_pict"]=result[5]
    cursor.close()
    conn.close()
    return my_dict

@app.put("/Update_User/")
async def update_user(Username: str, First_name:str, Last_name:str, Password:str):
    conn=sqlite3.connect("Userdatabase.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE users SET First_name = ?, Last_name = ?, Password = ?  WHERE Username = ?", 
    (First_name,Last_name,Password,Username))
    conn.commit()
    cursor.close()
    conn.close()

@app.get("/history/{Username}")
async def filter_history(Username: str):
    conn=sqlite3.connect("Userdatabase.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM history WHERE user = ?",(Username,))
    result=cursor.fetchall()
    to_return = []
    for row in result:
        row_dict = {
            'id': row[0],
            'username': row[1],
            'image': base64.b64encode(row[2]).decode('utf-8'),
            'crop': row[3],
            'stress': row[4],
            'confidence': row[5],
            'x1': row[6],
            'y1': row[7],
            'x2': row[8],
            'y2': row[9],
            'date': row[10],
            'time': row[11]
        }
        to_return.append(row_dict)
    
    cursor.close()
    conn.close()
    if not to_return:
        return [{
            'id': 9999,
            'username': Username,
            'image': bytearray(),
            'crop': 'No Data',
            'stress': 'No Data',
            'confidence': 0,
            'x1': 0,
            'y1': 0,
            'x2': 0,
            'y2': 0,
            'date': 0,
            'time': 0
        }]
    else:
        return to_return

@app.post("/addhistory")
async def add_history(username: str = Form(...),
                      image: UploadFile = File(...),
                      crop: str = Form(...),
                      stress: str = Form(...),
                      confidence: float = Form(...),
                      x1: int = Form(...),
                      y1: int = Form(...),
                      x2: int = Form(...),
                      y2: int = Form(...),
                      date: str = Form(...),
                      time: str = Form(...)):
    image_data = await image.read()
    byte_array = bytearray(image_data)
    
    data = (username, image_data, crop, stress, confidence, x1, y1, x2, y2, date, time)

    conn=sqlite3.connect("Userdatabase.db")
    cursor=conn.cursor()

    insert_query = '''
        INSERT INTO history (user, image, crop, stress, confidence, x1, y1, x2, y2, date, time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
    cursor.execute(insert_query, data)

    conn.commit()

    cursor.close()
    conn.close()

@app.post("/deleteuserhistory")
async def delete_user_history(username: str = Query(...)):
    conn = sqlite3.connect("Userdatabase.db")
    cursor = conn.cursor()

    delete_query = "DELETE FROM history WHERE user = ?"
    cursor.execute(delete_query, (username,))

    conn.commit()
    cursor.close()
    conn.close()

@app.post("/deletehistory")
async def delete_history(id: int = Query(...)):
    conn = sqlite3.connect("Userdatabase.db")
    cursor = conn.cursor()

    delete_query = "DELETE FROM history WHERE id = ?"
    cursor.execute(delete_query, (id,))

    conn.commit()
    cursor.close()
    conn.close()

@app.get("/allStress")
async def get_All():
    to_return = [d for d in stress_details]
    print(stress_details)
    return stress_details

@app.get("/image/{image_of}")
async def get_Image(image_of: str):
    to_open_image = "images/" + image_of + ".jpg"
    if os.path.exists(to_open_image):
        return FileResponse(to_open_image, media_type="image/jpg")
    else:
        to_open_image = "images/no_image.jpg"
        return FileResponse(to_open_image, media_type="image/jpg")
    
@app.get("/plant/image/{image_of}")
async def get_plant_image(image_of: str):
    to_open_image = "plantimage/" + image_of + ".jpg"
    if os.path.exists(to_open_image):
        return FileResponse(to_open_image, media_type="image/jpg")
    else:
        to_open_image = "plantimage/no_image.jpg"
        return FileResponse(to_open_image, media_type="image/jpg")
    
    

@app.get("/plant/{crop}")
async def get_Crop_Info(crop: str):
    crop = crop.lower()
    to_return = [d for d in plant_details if d.get("crop") == crop]
    return to_return



@app.get("/{crop}")
async def get_Crop(crop: str):
    to_return = []
    crop = crop.capitalize()
    to_return = [d for d in stress_details if d.get("Crop") == crop]
    return to_return
    # if crop == "onion":
    #     for i in range(len(onion_data.stress_dict)):
    #         to_return.append({"id": i, "stress": onion_data.stress_dict[i]})
    #     return to_return
    # elif crop == "corn":
    #     for i in range(len(corn_data.stress_dict)):
    #         to_return.append({"id": i, "stress": corn_data.stress_dict[i]})
    #     return to_return
    # elif crop == "Eggplant":
    #     for i in range(len(eggplant_data.stress_dict)):
    #         to_return.append({"id": i, "stress": eggplant_data.stress_dict[i]})
    #     return to_return
    # elif crop == "Tomato":
    #     for i in range(len(tomato_data.stress_dict)):
    #         to_return.append({"id": i, "stress": tomato_data.stress_dict[i]})
    #     return to_return
    # else:
    #     return {"message": f"{crop} no on the list"}
        

# @app.get("/Onion/{stress}")
# async def get_Onion(stress: str):
#     for i in onion_data.stress_dict:
#         if i['Stress'] == stress:
#             return i
#     else:
#         return {"message": "Stress not found"}
    
# @app.get("/Corn/{stress}")
# async def get_Corn(stress: str):
#     for i in corn_data.stress_dict:
#         if i['Stress'] == stress:
#             return i
#     else:
#         return {"message": "Stress not found"}
    
# @app.get("/Eggplant/{stress}")
# async def get_Eggplant(stress: str):
#     for i in eggplant_data.stress_dict:
#         if i['Stress'] == stress:
#             return i
#     else:
#         return {"message": "Stress not found"}
    
# @app.get("/Tomato/{stress}")
# async def get_Tomato(stress: str):
#     for i in tomato_data.stress_dict:
#         if i['Stress'] == stress:
#             return i
#     else:
#         return {"message": "Stress not found"}


# @app.post("/path")
# async def demo_post(inp: Msg):
#     return {"message": inp.msg.upper()}


# @app.get("/path/{path_id}")
# async def demo_get_path_id(path_id: int):
#     return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}