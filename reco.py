# Onion
onion_stress = ["Botrytis leaf blight", "Downy Mildew", "Armyworm", "Leaf Miner"]
onion_stressDesc = [ 
    """Botrytis leaf blight -  sometimes also referred to as Botrytis leaf spot, occurs on onions. 
    White, sunken spots on leaves are usually the first sign of infection. Spots are small, oval-shaped, and range from 0.06 to 0.25 inch (0.5–6 mm) long. 
    They sometimes have a light-green halo and may appear water-soaked. The epidermis around the spots may be silvery. 
    When numerous spots are present, leaf tips die back, and whole leaves may eventually die.""".replace('\n', ""),

    """Downy Mildew - At the field level, symptoms of downy mildew are first noticed as circular clumps of yellowed plants that are a few to many feet in diameter. 
    As the disease progresses, the yellowing patterns often enlarge in the direction of prevailing winds.
    On individual plants, leaf tissue becomes pale green, then tan to brown or yellow, and finally collapses. Lesions may exhibit a violet-to-purple color. 
    When leaves are wet, or when humidity is very high, signs of Peronospora destructor are visible on the surface of older leaves as fine, furry, grayish-white growths. 
    These growths may later turn purple or brown as a result of a secondary infection of the lesion by other fungi, 
    such as those that cause PURPLE BLOTCH AND STEMPYLIUM LEAF BLIGHT, as these fungi can produce purple pigmentation and dark spores.
    """.replace('\n', ""),

    """Armyworm -  is an early season pest that attacks grass crops like small grains and corn. It is not a common economic pest, 
    but occasionally can occur in high numbers and cause severe damage to seedlings and whorl stage corn. Armyworm, in field corn, 
    is always associated with the presence of grassy weeds within fields prior to planting or during the season. Moths will not lay eggs on corn plants but prefer 
    other grass plants.""".replace('\n', ""),
    """
    Leafminer - Adults have yellow heads, knees, sides of abdomens; otherwise mostly dark gray, just over 1/10 inch long.
    Pupae are red-brown, slightly longer than adults.
    Larvae are white to yellow, up to about 1/3 inch long.
    Eggs are white, about 1/50 inch long, found on leaves.
    Adult feeding holes found in rows, with milky white sap coming out.
    """.replace('\n', "")
    ]
onion_stressSoln = [

    # Botrytis leaf blight
    ["""There are several control methods available for managing Botrytis leaf blight in onions, including chemical, biological, and cultural control.
    
    Chemical Control: Copper fungicides: Copper fungicides are a common chemical treatment option for Botrytis Blight. 
    They disrupt the fungal cell walls and prevent the fungus from growing.Regular Pesticides: 
    Many effective pesticides against other fungi can also help control Botrytis Blight.
    Chlorothalonil: Chlorothalonil is a broad-spectrum fungicide that can prevent and control Botrytis Blight.
    
    Biological Control:Biological control is an environmentally friendly method of managing Botrytis leaf blight in onions. 
    The use of microbial agents such as Trichoderma spp., Bacillus subtilis, and Pseudomonas fluorescens has been found to be effective in controlling the disease. 
    These microbial agents work by competing with the pathogen for nutrients and space, and also by producing antimicrobial compounds that inhibit the growth of the pathogen.
    
    Cultural Control: Botrytis leaf blight, sometimes also referred to as Botrytis leaf spot, occurs on onions. 
    White, sunken spots on leaves are usually the first sign of infection. Spots are small, oval-shaped, and range from 0.06 to 0.25 inch (0.5–6 mm) long. 
    They sometimes have a light-green halo and may appear water-soaked. The epidermis around the spots may be silvery. 
    When numerous spots are present, leaf tips die back, and whole leaves may eventually die.""".replace('\n', "")], 

    # Downy Mildew
    ["""There are several control methods available for managing Downy mildew in onions, including chemical, biological, and cultural control.
    
    Chemical Control: Spray at the first sign of the disease. After the first spray, scout fields and make subsequent applications when weather conditions are favorable for the disease. 
    Rotate with fungicides from different mode-of-action groups to reduce the risk of fungicide resistance development. 
    Fungicides may be applied on a 7-day schedule (only as consistent with the label), if necessary. 
    For all fungicides, thorough coverage of foliage is important in the control of downy mildew. 
    Apply appropriate foliar fungicides taking care to apply thoroughly to waxy leaves. 
    Chlorothalonil and mancozeb are the main protectant fungicides for downy mildew.
    
    Biological Control: Seed treatment, as well as leaf spraying with Pseudomonas fluorescens, can be an effective measure for controlling downy mildew (4 to 5 g per kg of seed). 
    Seeds treated with this beneficial bacteria increase seedling strength and inhibit sporulation of the downy mildew pathogen. 
    Since the effectiveness is markedly higher, it is recommended to control downy mildew with P. fluorescens through seed treatment and leaf spraying.
    
    Cultural Control: Use a 3-year rotation away from Allium crops in fields where the disease has occurred. 
    Use disease-free bulbs, sets, and seed. Remove and destroy material of any Allium plants, including residue from the previous crop, volunteer plants, and culls from storage. 
    Avoid entering fields when leaves are wet. Avoid injuring the crop with herbicides and other.""".replace('\n', "")],

    # Armyworm
    ["""There are several control methods available for managing armyworms in onions, including chemical, biological, and cultural control.
    
    Chemical Control: Chemical control is the most common method of managing armyworms in onions. 
    The use of insecticides is recommended to control the pest. The most effective insecticides for controlling armyworms in onions include pyrethroids, organophosphates, and spinosyns. 
    These insecticides should be applied according to label instructions and at regular intervals to ensure effective control.
    
    Biological Control: Biological control is an environmentally friendly method of managing armyworms in onions. 
    The use of microbial agents such as Bacillus thuringiensis (Bt) and entomopathogenic nematodes has been found to be effective in controlling the pest. 
    These microbial agents work by infecting and killing the pest.
    
    Cultural Control: Cultural control is an effective method of managing armyworms in onions. 
    Cultural practices can be adopted through crop rotation by avoiding planting onions in the same field for consecutive seasons. 
    Remove and destroy crop debris from the field, early planting can reduce the incidence of the pest and proper plant spacing can reduce the incidence of the pest by increasing air circulation.
    """.replace('\n', "")],

    # Leaf Miner
    ["""There are several control methods available for managing leaf miners in onions, including chemical, biological, and cultural control.
    
    Chemical Control: Pyrethrin, an organic pesticide, will kill leaf miners as they leave the egg and enter the leaf. 
    Since they have to chew into the leaf, they ingest the poison with the leaf and die. 
    However, pyrethrin also kills good insects such as bees and leaf miner predators. 
    Use to spot-treat concentrations of leaf miners rather than blanket the whole garden. Be sure you get it on the bottom side of the leaf.
    
    Biological Control: is an environmentally friendly method of managing leaf miners in onions. 
    The use of parasitic wasps such as Diglyphus isaea has been found to be effective in controlling the pest. 
    These parasitic wasps work by laying their eggs inside the pest, which leads to its death.
    
    Cultural Control: is an effective and environmentally friendly method of managing leaf miners on onions, 
    which involves the adoption of various agricultural practices such as crop rotation, sanitation, mulching, plant spacing, 
    and plant selection to reduce the incidence of the pest, promote crop health, and ultimately increase yield.
    """.replace('\n', "")]
]


# Eggplant
eggplant_stress = ["Cercospora leaf spot", "Powdery Mildew", "Armyworm", "Leaf Miner", "Aphids", "Flea beetle", "White Flies", "Potato Beetle", "Leaf roller moth"]
eggplant_stressDesc = [ 
    #Cercospora leaf spot
    """Cercospora leaf spot is a fungal disease that affects eggplants, causing brown or grayish lesions on the leaves. 
    These lesions may have a yellow halo around them and can eventually cause the leaves to fall off.""".replace('\n', ""),

    #Powdery Mildew
    """Powdery mildew is a fungal disease that affects a wide range of plants, including eggplants. 
    It appears as a white or grayish powdery coating on the leaves, stems, and sometimes flowers of plants. 
    As the disease progresses, the coating can become thicker, causing the plant to appear whitewashed. 
    In severe cases, the leaves can turn yellow, brown, or even black, and the affected parts of the plant may become distorted or stunted. 
    Powdery mildew thrives in warm, humid environments, and can spread rapidly under these conditions.""".replace('\n', ""),

    #Armyworm
    """Armyworms are the larvae of certain species of moths that can cause significant damage to eggplants and other crops. 
    These larvae are usually green, brown, or black in color, with distinct stripes along their body. 
    They are called "armyworms" because they move in large groups, devouring plants as they go. 
    The larvae can grow up to two inches long and can consume large amounts of foliage, causing defoliation and stunting of the plants.

    Armyworms are most active during the night and can be difficult to spot during the day. 
    Early signs of armyworm infestation on eggplants include chewed leaves, holes in leaves, and stripped stems. 
    If left unchecked, the armyworms can quickly defoliate entire plants and spread to neighboring crops. """.replace('\n', ""),

    #Leaf Miner
    """Leaf miners are the larvae of certain fly species that feed on the leaf tissue of eggplants and other plants. 
    They create winding tunnels or "mines" that appear as white or brownish lines on the leaves, and can cause significant damage to the plant's ability to photosynthesize. 
    Leaf miner damage can result in wilting, stunting, and decreased crop yield.
    
    Leaf miners are difficult to control once they have become established, as the larvae are protected within the leaf tissue. Early detection is key to preventing their spread. 
    Signs of leaf miner infestation on eggplants include the appearance of winding tunnels on the leaves, and small black flies hovering around the plants.""".replace('\n', "")

    #Aphids
    """Aphids are small, soft-bodied insects that can infest eggplants and other plants, feeding on the sap of the plant. 
    They are typically green, yellow, or black in color and have pear-shaped bodies with long antennae. 
    Aphids can reproduce rapidly and in large numbers, causing damage to plants by sucking the sap and excreting honeydew, which can attract ants and lead to the growth of black sooty mold.
    
    Signs of aphid infestation on eggplants include the presence of the insects themselves, distorted or curled leaves, and the appearance of honeydew or sooty mold on the leaves. 
    Aphids can also transmit viral diseases to plants, further reducing their health and yield.""".replace('\n', ""),

    #Flea beetle
    """Flea beetles are small, jumping insects that can cause damage to eggplants and other plants by feeding on the leaves and stems. 
    They are typically black or brown in color and are named for their ability to jump like fleas when disturbed. 
    Flea beetles can cause significant damage to eggplants, especially when populations are high.
    
    Signs of flea beetle damage on eggplants include small holes in the leaves, a "shot hole" appearance of the foliage, and wilting or stunted growth. 
    Flea beetles can also transmit bacterial wilt disease to eggplants, further reducing their health and yield.""".replace('\n', ""),

    #White Flies
    """Whiteflies are small, sap-sucking insects that can infest eggplants and other plants, causing damage to the foliage and reducing the plant's ability to photosynthesize. 
    They are named for their white, moth-like appearance and are typically found on the undersides of leaves. 
    Whiteflies can also excrete honeydew, which can lead to the growth of sooty mold on the leaves.
    
    Signs of whitefly infestation on eggplants include the presence of the insects themselves, distorted or yellowed leaves, and the appearance of honeydew or sooty mold on the leaves. 
    Whiteflies can also transmit viral diseases to plants, further reducing their health and yield.""".replace('\n', ""),

    #Potato Beetle
    """Potato beetles, also known as Colorado potato beetles, are a common pest of eggplants and other members of the nightshade family. 
    They are yellow and black striped and have a distinctive hard shell. Adult beetles and their larvae can cause significant damage to eggplant foliage, feeding on the leaves and stems of the plant.
    
    Signs of potato beetle infestation on eggplants include the presence of the insects themselves, skeletonized leaves, and defoliation of the plant. 
    Potato beetles can also transmit viral diseases to plants, further reducing their health and yield.
    """.replace('\n', ""),

    # Leaf roller moth
    """Leaf roller moth is a common pest that feeds on eggplants, causing significant damage to the plants. 
    The larvae of the moth feed on the leaves, creating characteristic tunnels or rolled-up leaves. 
    The damage caused by leaf roller moths can lead to reduced yields and poor plant growth.
    
    To control leaf roller moths on eggplants, it's important to implement an integrated pest management (IPM) approach that combines different control methods. 
    This can include cultural control methods, such as crop rotation and sanitation, as well as biological control methods, such as the use of natural predators or parasites. Chemical control methods can also be used, but should be used judiciously to minimize the impact on non-target organisms and the environment.
    """.replace('\n', ""),
    ]
eggplant_stressSoln = [

    # Cercospora leaf spot
    ["""There are several control methods available for managing Cercospora leaf spot on eggplants, including chemical, biological, and cultural control.
    
    Chemical Control: The use of fungicides is recommended to control the disease. 
    The most effective fungicides for controlling Cercospora leaf spot on eggplants include chlorothalonil, copper-based fungicides, and azoxystrobin. 
    These fungicides should be applied according to label instructions and at regular intervals to ensure effective control.
    
    Biological Control: The use of beneficial microorganisms such as Trichoderma harzianum and Bacillus subtilis has been found to be effective in controlling the disease. 
    These beneficial microorganisms work by competing with the fungal pathogen for nutrients, and also by producing antifungal compounds that inhibit its growth.
    
    Cultural Control: Avoid planting eggplants in the same field for consecutive seasons. 
    Proper plant spacing can reduce the incidence of the disease by increasing air circulation. 
    Remove and destroy infected plant debris to reduce the disease inoculum. 
    Avoid overhead irrigation as it can increase the humidity in the field, which favors disease development. 
    Proper fertilization can help keep the plants healthy and better able to resist the disease.
    """.replace('\n', "")],

    # Powdery Mildew
    ["""There are several control methods available for managing powdery mildew on onions, including chemical, biological, and cultural control.
    
    Chemical Control: The use of fungicides is recommended to control the disease. 
    The most effective fungicides for controlling powdery mildew on eggplants include sulfur, azoxystrobin, and trifloxystrobin. 
    These fungicides should be applied according to label instructions and at regular intervals to ensure effective control.
    
    Biological Control:Natural enemies of powdery mildew, such as predatory mites, can be used to control its spread. 
    These natural enemies can be introduced into the eggplant field, either by releasing them or by creating habitats that encourage their presence. 
    Additionally, several fungal species can be used to control powdery mildew. These fungi infect the powdery mildew and eventually kill it.
    
    Cultural Control: Avoid overhead irrigation as it can increase the humidity in the field, which favors disease development. 
    Proper plant spacing can reduce the incidence of the disease by increasing air circulation. 
    Ensure that the soil pH is maintained between 6.0 and 7.0, as this can help reduce the incidence of the disease. 
    Proper fertilization can help keep the plants healthy and better able to resist the disease. 
    Avoid planting eggplants in the same field for consecutive seasons.
    """.replace('\n', "")],

    # Armyworm
    ["""There are several control methods available for managing Armyworm spot on eggplants, including chemical, biological, and cultural control.
    
    Chemical Control: Some common pesticides used to control armyworms in eggplants include carbaryl, malathion, and permethrin. 
    It is important to follow the instructions on the label and use the appropriate protective equipment while applying the pesticide. 
    It is also important to use pesticides responsibly and only when necessary, as overuse of pesticides can harm the environment and non-target organisms.
    
    Biological Control: Some natural enemies of armyworms include parasitic wasps, predatory beetles, and birds. 
    One effective biological control method for armyworms is releasing trichogramma wasps, which lay their eggs inside armyworm eggs, preventing them from hatching. 
    Another method is releasing nematodes, which infect and kill the armyworms. This method is safe for the environment and does not harm other beneficial insects.
    
    Cultural Control: Involves modifying the environment to reduce the population of armyworms. 
    One method is to remove and destroy any plant debris, as this can provide a breeding ground for armyworms. 
    Another method is to practice crop rotation, as armyworms prefer to feed on certain plants and may not survive if their preferred host is not present. 
    Additionally, planting resistant varieties of eggplants can also help control armyworms.""".replace('\n', "")],

    # Leaf Miner
    ["""There are several control methods available for managing Leaf Miner on eggplants, including chemical, biological, and cultural control.

    Chemical Control: Some common pesticides used to control leaf miners in eggplants include spinosad, neem oil, and pyrethroids. 
    It is important to follow the instructions on the label and use the appropriate protective equipment while applying the pesticide. 
    However, repeated use of pesticides can lead to the development of resistance in leaf miners and can also harm beneficial insects, such as bees and other pollinators.
    
    Biological Control: Natural enemies of leaf miners include parasitic wasps, predatory beetles, and spiders. 
    One effective biological control method for leaf miners is releasing parasitic wasps that lay their eggs inside the leaf miner larvae, killing them. 
    Another method is releasing predatory mites, which feed on the leaf miner eggs and larvae. This method is safe for the environment and does not harm other beneficial insects.
    
    Cultural Control: One method is to remove and destroy any infested leaves, as this can reduce the number of leaf miners. 
    Another method is to use row covers to prevent adult leaf miners from laying eggs on the plants. Additionally, planting resistant varieties of eggplants can also help control leaf miners.
    """.replace('\n', "")],

    # Aphids
    ["""There are several control methods available for managing Aphids on eggplants, including chemical, biological, and cultural control.

    Chemical Control: Some common pesticides used to control aphids in eggplants include insecticidal soaps, neem oil, and pyrethroids. 
    It is important to follow the instructions on the label and use the appropriate protective equipment while applying the pesticide. However, repeated use of pesticides can lead to the development of resistance in aphids and can also harm beneficial insects, such as bees and other pollinators.
    
    Biological Control: Some natural enemies of aphids include lady beetles, lacewings, and parasitic wasps. One effective biological control method for aphids is releasing lady beetles, which feed on the aphids and their eggs. Another method is releasing lacewings, which feed on both aphids and other pest insects. This method is safe for the environment and does not harm other beneficial insects.
    
    Cultural Control: One method is to remove and destroy any infested leaves or plants, as this can reduce the number of aphids. Another method is to use reflective mulches, which can disorient aphids and prevent them from finding the plants. Additionally, planting companion plants, such as marigolds or garlic, can also help control aphids.
    """.replace('\n', "")],

    # Flea beetle
    ["""There are several control methods available for managing Flea beetle on eggplants, including chemical, biological, and cultural control.

    Chemical Control: Some common pesticides used to control flea beetles in eggplants include carbaryl, pyrethroids, and neonicotinoids. It is important to follow the instructions on the label and use the appropriate protective equipment while applying the pesticide. However, repeated use of pesticides can lead to the development of resistance in flea beetles and can also harm beneficial insects, such as bees and other pollinators.
    
    Biological Control: Natural enemies of flea beetles include parasitic wasps and predatory insects like ladybugs. One effective biological control method for flea beetles is releasing beneficial nematodes in the soil. These microscopic worms will attack the larvae of the flea beetles, reducing their population.
    
    Cultural Control: One method is to use row covers to physically exclude the beetles from the plants. Another method is to plant eggplants earlier in the season, as flea beetles tend to be more active in late spring and early summer. Additionally, removing any weeds or debris around the plants can also help reduce the population of flea beetles.
    """.replace('\n', "")],

    # White Flies
    ["""There are several control methods available for managing White Flies on eggplants, including chemical, biological, and cultural control.

    Chemical Control: Using chemical insecticides can help control whiteflies, but it's important to use them carefully and in accordance with the instructions on the label. Some insecticides that may be effective against whiteflies on eggplants include neonicotinoids, pyrethroids, and insecticidal soaps. Always follow the instructions on the label carefully and avoid spraying during the heat of the day, which can cause damage to the plants. Make sure to follow any recommended waiting periods before harvesting.
    
    Biological Control: Using natural predators or parasites to control the whitefly population. Some examples of biological control agents that can be effective against whiteflies on eggplants include ladybugs, lacewings, and parasitic wasps. These can be purchased from garden supply stores or online and released onto your eggplants. Some companion plants such as marigolds or alyssum can also attract beneficial insects to the garden.
    
    Cultural Control: Remove weeds around your eggplants, which can harbor whiteflies. You can also try using row covers or netting to physically block whiteflies from accessing your plants. Regularly checking your plants for signs of infestation and removing any affected leaves can also help prevent the spread of whiteflies.
    """.replace('\n', "")],

    # Potato Beetle
    ["""There are several control methods available for managing Potato Beetle on eggplants, including chemical, biological, and cultural control.

    Chemical Control: Insecticides that may be effective include pyrethroids, neonicotinoids, and spinosad. Always follow the instructions on the label carefully and avoid spraying during the heat of the day, which can cause damage to the plants. Make sure to follow any recommended waiting periods before harvesting.
    
    Biological Control: Examples of biological control agents that can be effective against potato beetles on eggplants include ladybugs, lacewings, and parasitic wasps. These can be purchased from garden supply stores or online and released onto your eggplants. Some companion plants such as dill, cilantro, or parsley can attract beneficial insects to the garden.
    
    Cultural Control: Practice crop rotation and avoid planting eggplants in the same location each year. You can also try using row covers or netting to physically block potato beetles from accessing your plants. Regularly checking your plants for signs of infestation and removing any affected leaves can also help prevent the spread of potato beetles.
    """.replace('\n', "")],

    # Leaf roller moth
    ["""There are several control methods available for managing Leaf roller moth on eggplants, including chemical, biological, and cultural control.
    
    Chemical Control: There are many chemical insecticides available that can be used to control leaf roller moths, such as pyrethroids, neonicotinoids, and organophosphates. However, it's important to use these pesticides judiciously and follow the label instructions carefully to avoid harming non-target organisms and to minimize the environmental impact.
    
    Biological Control: One example of biological control is the use of Trichogramma wasps, which lay their eggs in the eggs of the leaf roller moths, preventing them from hatching. Other natural predators, such as lacewings, ladybugs, and parasitic wasps, can also be used to control leaf roller moths.
    
    Cultural Control: Involves modifying the environment to make it less favorable for the development and survival of leaf roller moths. This can include practices such as crop rotation, weed control, and sanitation. For example, removing plant debris and fallen fruits from the field can help reduce the number of overwintering sites for the leaf roller moth.
    """.replace('\n', "")]
]

# Corn
corn_stress = ["Leaf Spot", "Powdery Mildew", "Armyworm", "Leaf Miner", " Corn Borer", "Eye Spot", "White Flies", "Corn borer midrib feeding"]
corn_stressDesc = [ 
    #Leaf Spot
    """Leaf spot is a common disease that affects corn plants. It is caused by several different fungal pathogens, including Helminthosporium spp., Cercospora spp., and Bipolaris spp. 
    Symptoms of leaf spot typically appear as small, circular lesions on the leaves, which can be surrounded by a yellow halo.
    
    If left untreated, leaf spot can cause significant damage to corn plants, reducing yield and overall plant health. 
    To manage leaf spot, it is important to implement a combination of cultural and chemical control measures.
    """.replace('\n', ""),

    #Powdery Mildew
    """Powdery mildew is another common fungal disease that can affect corn plants. The disease is caused by the fungus Erysiphe orontii and appears as a white, powdery coating on the leaves, stalks, and tassels of the plant.
    
    The powdery mildew fungus thrives in warm, humid conditions, and can spread rapidly if left unchecked. In addition to reducing yield, powdery mildew can also lead to premature plant death and susceptibility to other diseases.
    """.replace('\n', ""),

    #Armyworm
    """Armyworms are the larvae of certain species of moths that can cause significant damage to corn crops. They are named for their behavior of moving in large groups and devouring everything in their path, much like an army on the march.
    
    Armyworms are typically about 1-2 inches in length and can be brown, gray, or green in color. They have distinct stripes on their bodies that run the length of their back and sides. Armyworms feed on the leaves, stalks, and ears of corn plants, causing damage that can range from minor to severe.
    """.replace('\n', ""),

    #Leaf Miner
    """Leaf miners are small insects that can cause damage to corn plants by feeding on the leaves. They are typically the larvae of small, black and yellow flies known as Agromyzidae.
    
    The adult leaf miner flies lay eggs on the underside of corn leaves, and when the eggs hatch, the larvae burrow into the leaf tissue and feed on the plant's sap. This feeding creates characteristic white or yellowish "mines" or tunnels within the leaves, which can lead to discoloration and a decrease in plant health and vigor.
    
    The damage caused by leaf miners on corn is typically not severe, but it can weaken the plant and make it more susceptible to other pests and diseases. In addition, heavy infestations of leaf miners can reduce the plant's ability to photosynthesize and produce energy, which can ultimately impact yield.
    """.replace('\n', ""),

    #Corn Borer
    """Corn borers are a common pest that can cause significant damage to corn crops. They are the larvae of moths that lay their eggs on the leaves of corn plants. When the eggs hatch, the larvae burrow into the stalks or ears of the corn plant and feed on the tissue inside.
    Corn borer damage can cause the plant to become stunted and weakened, and it can also make the plant more susceptible to other pests and diseases. The damage can also lead to yield losses if left unchecked.
    """.replace('\n', ""),

    #Eye Spot
    """Eye spot is a fungal disease that can affect corn plants. It is caused by the fungus Aureobasidium zeae and can cause significant damage to the leaves and stalks of the plant.
    
    Eye spot appears as small, circular lesions on the corn leaves. These lesions can range in color from tan to reddish-brown and are surrounded by a yellowish halo. As the disease progresses, the lesions can coalesce and cause the leaf tissue to die and turn brown. In severe cases, the disease can also infect the stalks of the corn plant, causing lodging and yield losses.
    """.replace('\n', ""),

    #White Flies
    """Whiteflies are small, winged insects that can cause damage to corn crops by feeding on the sap of the plant. They are typically found on the underside of the leaves and can be identified by their white or yellow color and small size.
    
    Whiteflies can cause damage to corn plants by feeding on the sap, which can cause yellowing of the leaves, stunted growth, and decreased yield. They can also transmit viruses to the plant, which can further reduce its health and vigor.
    """.replace('\n', ""),

    #Corn borer midrib feeding
    """Corn borer midrib feeding is a type of damage caused by the larvae of the corn borer moth that feed on the midrib of corn leaves. The midrib is the central vein that runs through the center of the leaf.
    
    When corn borer larvae feed on the midrib of corn leaves, they can cause significant damage to the plant. The feeding can cause the leaves to wilt and curl, and it can also make the plant more susceptible to other pests and diseases.
    
    The larvae of the corn borer moth are usually about 1 inch long and can be light pink or greenish-white in color. They can be found feeding on the midrib and inside the stalks or ears of the corn plant.
    """.replace('\n', "")
    ]

corn_stressSoln = [
    # Leaf Spot
    ["""To control leaf spot on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.

    Chemical Control: There are numerous fungicides available for control of Gray leaf spot.  
    However, there is no guarantee that fungicide applications will result in economic returns, especially if they are applied to highly resistant hybrids in fields with little disease.  For this reason it is important to scout fields for symptoms of Gray leaf spot and apply fungicides only when they are needed.  Scouts should pay particular attention to the lower three leaves of the corn plant from the period just before tasseling to two weeks after tasseling.  If at least 50% of plants in a field have disease present on the third leaf below the ear leaf or higher prior to tasseling, the hybrid is susceptible, and the conditions are favorable for disease, then a spray may be warranted.  Gray leaf spot severity is unpredictable and multiple factors should be considered when making the decision to use fungicides to control Gray leaf spot.  Always follow label directions when applying a fungicide.
    
    Biological Control: Involves the use of natural enemies, such as beneficial microorganisms, to control leaf spot. One example of biological control is the use of biocontrol agents, such as Trichoderma spp., Bacillus spp., or Pseudomonas spp., which can colonize the plant's roots and leaves, and produce antifungal compounds that suppress the growth of leaf spot pathogens.
    
    Cultural Control: Involves modifying the environment to make it less favorable for the development and spread of leaf spot. This can include practices such as crop rotation, planting resistant varieties, and sanitation. For example, removing infected plant debris and avoiding overhead irrigation can help reduce the spread of leaf spot. Other cultural practices that can help prevent leaf spot infections include planting corn in well-drained soil, avoiding planting corn in fields with a history of leaf spot infections and providing proper nutrition and avoiding over-fertilization, which can increase susceptibility to leaf spot.
    """.replace('\n', "")], 

    # Powdery Mildew
    ["""To control Powdery Mildew on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
     Chemical Control: There are many fungicides available that can be used to control powdery mildew on corns, such as sulfur, triazoles, and strobilurins. 
     However, it's important to use these fungicides judiciously and follow the label instructions carefully to avoid harming non-target organisms and to minimize the environmental impact.
     
     Biological Control: Biological control involves the use of natural enemies, such as beneficial microorganisms, to control powdery mildew. 
     One example of biological control is the use of biocontrol agents, such as Trichoderma spp. and Bacillus spp., which can colonize the plant's roots and leaves, 
     and produce antifungal compounds that suppress the growth of powdery mildew pathogens.
     
     Cultural Control: Practices such as crop rotation, planting resistant varieties, and sanitation. 
     For example, removing infected plant debris and avoiding overhead irrigation can help reduce the spread of powdery mildew. 
     Other cultural practices that can help prevent powdery mildew infections include planting corn in well-drained soil, avoiding planting corn in fields with a history of powdery mildew infections, 
     and Providing proper nutrition and avoiding over-fertilization, which can increase susceptibility to powdery mildew.
    """.replace('\n', "")],

    # Armyworm
    ["""To control Armyworm on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
    Chemical Control: There are many insecticides available that can be used to control armyworms on corns, such as pyrethroids, carbamates, and organophosphates. 
    However, it's important to use these insecticides judiciously and follow the label instructions carefully to avoid harming non-target organisms and to minimize the environmental impact.
    
    Biological Control: One example of biological control is the use of parasitic wasps or flies that lay their eggs in the armyworm's eggs or larvae, causing their death. Another example is the use of insect-killing fungi, such as Beauveria bassiana, which can infect and kill armyworms.
    
    Cultural Control: Cultural control involves modifying the environment to make it less favorable for the development and spread of armyworms. This can include practices such as crop rotation, planting resistant varieties, and sanitation. 
    For example, removing crop residues and weeds from the field can help reduce the population of armyworms, planting corn early in the season to avoid peak armyworm activity.
    
    """.replace('\n', "")],

    # Leaf Miner
    ["""To control Leaf Miner on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
     Chemical Control: Chemical control involves the use of insecticides to prevent or treat leaf miner infestations. There are many insecticides available that can be used to control leaf miners on corns, such as pyrethroids, carbamates, and organophosphates. However, it's important to use these insecticides judiciously and follow the label instructions carefully to avoid harming non-target organisms and to minimize the environmental impact.
     
     Biological Control: One example of biological control is the use of parasitic wasps or flies that lay their eggs in the leaf miner larvae, causing their death. Another example is the use of insect-killing fungi, such as Beauveria bassiana, which can infect and kill leaf miners.
     
     Cultural Control: Cultural control involves implementing farming practices that discourage pest infestations. Some cultural practices that can help control leaf miner on corns include planting corn in different fields each year to reduce pest build-up, early planting can help avoid peak leaf miner populations, regular weeding which helps to remove alternative host plants and reduce leaf miner populations.
    """.replace('\n', "")],

    # Corn Borer
    ["""To control Corn Borer on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
    Chemical Control: There are several insecticides that are effective against corn borers, including chlorpyrifos, bifenthrin, and cypermethrin. It is important to follow the label instructions carefully and apply insecticides when corn borers are in their most susceptible stages.
    
    Biological Control: One such natural enemy is the Trichogramma wasp, which lays its eggs in the eggs of corn borers, preventing them from hatching. Another natural enemy is the Bacillus thuringiensis (Bt) bacterium, which produces a toxin that is lethal to corn borers.
    
    Cultural Control: Cultural control involves using practices that make the environment less favorable for corn borers. Some strategies include choosing corn hybrids that have been bred for resistance to corn borers can reduce the need for chemical or biological control, planting corn early or late in the season can reduce the risk of corn borer infestations, and plowing or disking the soil can disrupt corn borer overwintering sites and reduce populations.


    """.replace('\n', "")],

    # Eye Spot
    ["""To control Eye spot on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
     Chemical Control: Fungicides such as azoxystrobin, pyraclostrobin, and propiconazole are effective against eye spot. It is important to follow the label instructions carefully and apply fungicides when eye spot is first detected or when conditions are favorable for disease development.
     
     Biological Control: One such natural enemy is the Trichoderma fungus, which is known to colonize the roots of corn plants and suppress eye spot. Other beneficial microorganisms such as mycorrhizae and rhizobacteria can also help reduce eye spot infections.
     
     Cultural Control: Cultural control involves using practices that make the environment less favorable for corn borers. Some strategies include planting a non-host crop, such as soybeans, in between corn crops can reduce eye spot populations, planting corn varieties that are resistant to eye spot can reduce the need for chemical or biological control, and plowing or disking the soil can help bury infected corn debris and reduce the risk of eye spot infections.


    """.replace('\n', "")],

    # White Flies
    ["""To control White Flies on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
     Chemical Control: Insecticides such as pyrethroids, neonicotinoids, and organophosphates are effective against whiteflies. It is important to follow the label instructions carefully and apply insecticides when whitefly populations are in their most susceptible stages.
     
     Biological Control: One such natural enemy is the parasitic wasp Encarsia formosa, which lays its eggs inside whitefly nymphs, killing them. Other beneficial insects such as ladybugs and lacewings can also help reduce whitefly populations.
     
     Cultural Control: Cultural control involves using practices that make the environment less favorable for whiteflies. Some strategies include Removing infected plant material wherein whiteflies can reproduce on infected plant material, so it is important to remove infected plants as soon as possible. Using reflective mulch can make it more difficult for whiteflies to locate plants to infest, planting flowers or other plants that attract beneficial insects can help reduce whitefly populations, and using row covers can physically exclude whiteflies from corn plants.

    """.replace('\n', "")],

    # Corn borer midrib feeding
    [""" To control Corn borer midrib feeding on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
     Chemical Control: There are several insecticides that are effective against corn borer midrib feeding, including chlorpyrifos, bifenthrin, and cypermethrin. It is important to follow the label instructions carefully and apply insecticides when corn borer midrib feeding is in its most susceptible stage.
     
     Biological Control: One such natural enemy is the Trichogramma wasp, which lays its eggs in the eggs of corn borers, preventing them from hatching. Another natural enemy is the Bacillus thuringiensis (Bt) bacterium, which produces a toxin that is lethal to corn borers.
     
     Cultural Control: Cultural control involves using practices that make the environment less favorable for corn borer midrib feeding. Some strategies include plowing or disking the soil can disrupt corn borer midrib feeding overwintering sites and reduce populations, planting corn early or late in the season can reduce the risk of corn borer midrib feeding infestations, and choosing corn hybrids that have been bred for resistance to corn borer midrib feeding can reduce the need for chemical or biological control.
    """.replace('\n', "")]

]

# Tomato
tomato_stress = ["Powdery Mildew", "Black Mold", "Fusarium Wilt", "Leaf Miner"]
tomato_stressDesc = [ 
    """Powdery mildew is a common fungal disease that can affect tomato plants, causing significant damage to the leaves, stems, and fruits. The disease is characterized by a white, 
    powdery growth on the surface of the plant, which can spread rapidly and cause the plant to become stunted and weakened. Some common symptoms of powdery mildew on tomato plants include white, 
    powdery growth on the leaves, stems, and fruits of the plant, yellowing of the leaves and premature leaf drop, curling of the leaves and distortion of the plant's growth, and stunted growth and reduced yields of fruit.
    """.replace('\n', ""),
    
    """Black mold on tomato plants is typically caused by a fungal infection, commonly known as "black mold" or "black spot." The fungus responsible for this condition is called Alternaria solani. 
    Symptoms of black mold on tomato plants may include black or brownish lesions or spots on leaves, stems, and fruit. These spots may be circular or irregular in shape, and may be raised or sunken. 
    The infected tissue may become dry and papery, and may eventually crack or crumble. As the infection progresses, the leaves may yellow and die, and the fruit may become distorted or mummified. 
    In severe cases, the plant may become stunted and eventually die. Black mold on tomatoes can spread rapidly under warm and humid conditions, making it important to control the infection as soon as it is detected.
    """.replace('\n', ""),
    
    """Fusarium wilt is a common fungal disease that affects tomato plants. The disease is caused by the fungus Fusarium oxysporum and can be devastating to tomato crops. 
    Symptoms of fusarium wilt on tomato plants usually begin with yellowing and wilting of the lower leaves, which may appear to be scattered throughout the plant. The yellowing may progress to the entire plant, causing it to wilt and eventually die.
    
    The fungus can survive in the soil for several years, making crop rotation an important management strategy. Fusarium wilt can also be transmitted through infected seeds, transplants, and soil. The fungus invades the roots of the tomato plant, interfering with the uptake of water and nutrients, which can lead to wilting and eventual death.
    """.replace('\n', ""),
    
    """Leaf miner is a common pest that affects tomato plants, as well as many other plants. The pest is a small, flying insect that lays eggs on the surface of the tomato plant leaves. When the eggs hatch, the larvae tunnel into the leaves, creating winding, white or yellowish-brown tracks or tunnels. These tunnels can cause significant damage to the leaves, interfering with the plant's ability to photosynthesize and produce healthy fruit.
    
    In addition to the visible tunnels, leaf miner damage can cause the leaves to become distorted or curled, which can further impact the plant's health. Severe infestations can result in stunted growth and reduced yield. Leaf miners typically thrive in warm, humid conditions, and can be difficult to control once established.
    """.replace('\n', "")
    ]

tomato_stressSoln = [
    #Powdery Mildew
    ["""To control Powdery Mildew on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
     
    Chemical control: There are several fungicides available that can control powdery mildew on tomato plants, including copper fungicides, sulfur fungicides, and fungicides containing potassium bicarbonate or neem oil. 
    Follow the instructions on the fungicide label carefully, as overuse or misuse can lead to plant damage or residue on the tomatoes. Avoid applying fungicides during the hottest part of the day or when the plants are water-stressed.
    
    Biological control: Biological control involves the use of natural enemies to control powdery mildew. One effective method is to apply a biofungicide containing Bacillus subtilis, a beneficial bacterium that can prevent powdery mildew from spreading. 
    Another option is to use predatory mites, such as Phytoseiulus persimilis or Neoseiulus californicus, which feed on powdery mildew and other plant pests.
    
    Cultural control: Planting resistant tomato varieties that are less susceptible to powdery mildew. Providing proper air circulation by spacing plants adequately and removing any plant debris or weeds that can harbor the fungus. 
    Watering the plants in the morning and avoiding overhead watering, which can promote fungal growth. Fertilizing the plants properly, as excessive nitrogen can increase susceptibility to powdery mildew. Using reflective mulches or coatings, such as kaolin clay, which can reduce the incidence of powdery mildew by reflecting sunlight and reducing leaf surface temperatures."""
    .replace('\n', "")],
    
    #Black mold
    ["""To control Black Mold on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
    Chemical control: There are several fungicides available that can control black mold on tomato plants, including copper fungicides, sulfur fungicides, and fungicides containing triadimefon or myclobutanil. Follow the instructions on the fungicide label carefully, as overuse or misuse can lead to plant damage or residue on the tomatoes. Avoid applying fungicides during the hottest part of the day or when the plants are water-stressed.
     
    Biological control: One effective method is to apply a biofungicide containing Bacillus subtilis, a beneficial bacterium that can prevent black mold from spreading. Another option is to use predatory mites, such as Phytoseiulus persimilis or Neoseiulus californicus, which feed on black mold and other plant pests.
     
    Cultural control: Reducing insect infestations, as insects such as aphids and whiteflies secrete a sticky substance called honeydew, which can promote the growth of black mold. Washing off the honeydew and black mold with a strong stream of water. Pruning infected branches or leaves and disposing of them in the trash. Using reflective mulches or coatings, such as kaolin clay, which can reduce the incidence of black mold by reflecting sunlight and reducing leaf surface temperatures.
    """.replace('\n', "")],
    
    #fusarium
    ["""To control Fusarium Wilt on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
    Chemical control: There are no chemicals available to cure fusarium wilt, but some fungicides can help reduce the severity of the disease. Fungicides containing chlorothalonil, mancozeb, or copper can help protect plants from fungal infections. Follow the instructions on the fungicide label carefully, as overuse or misuse can lead to plant damage or residue on the tomatoes.
     
    Biological control: One effective method is to use soil-borne beneficial microorganisms, such as Trichoderma spp. or Bacillus subtilis, which can suppress the growth of the fungus that causes fusarium wilt. Another option is to use soil solarization, a process that involves covering the soil with plastic to trap heat and kill the fungus.
     
    Cultural control: Planting resistant tomato varieties that are less susceptible to fusarium wilt. Rotating crops, as the fungus can survive in the soil for several years and infect future tomato crops. Removing and destroying infected plants and any plant debris that can harbor the fungus. Avoiding overwatering and watering at the base of the plants rather than overhead watering, which can promote fungal growth. Using sterilized soil or soilless growing media to start seedlings. Applying organic matter, such as compost, to the soil to promote a healthy microbial community.
    """.replace('\n', "")],
    
    #leaf miner
    ["""To control Leaf Miner on corns, there are several methods that can be used, including chemical control, biological control, and cultural control.
    Chemical control: There are several insecticides available that can control leaf miners on tomato plants, including spinosad, abamectin, and cyromazine. Follow the instructions on the insecticide label carefully, as overuse or misuse can lead to plant damage or residue on the tomatoes. Avoid applying insecticides during the hottest part of the day or when the plants are water-stressed.
     
    Biological control: Biological control involves the use of natural enemies to control leaf miners. One effective method is to release parasitic wasps, such as Diglyphus spp. or Chrysocharis spp., which lay their eggs in the leaf miner larvae, killing them. Another option is to use predatory mites, such as Phytoseiulus persimilis or Neoseiulus californicus, which feed on leaf miners and other plant pests.
     
    Cultural control: Removing and destroying any infected leaves or plant debris that can harbor the insects. Using reflective mulches or coatings, such as aluminum foil or silver plastic, which can confuse the leaf miners and reduce their attraction to the plants. Using yellow sticky traps, which can attract and trap adult leaf miner flies. Planting resistant tomato varieties that are less susceptible to leaf miners.
    """.replace('\n', "")]
]