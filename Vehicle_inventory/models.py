from fastapi import HTTPException
import json

vehicles=[]
file= "vehicle.json"

with open (file, "r") as f:
    data=f.read()
    vehicles=json.loads(data)
    
def filter_vehicles_id( vehicle_id):
    try:
        for vehicle in vehicles:
            if vehicle_id and vehicle.get("vehicle_id") == vehicle_id:
                return {"vehicle": vehicle}
        else:
            raise HTTPException(status_code=404, detail="No Vehicle found with the given parameters")
    except HTTPException as e:
        return {"error": e}
    

def filter_vehicles (make , model , price_range):
    try:

        filtered_vehicles = []
    
        for vehicle in vehicles:

            if make and make.lower() not in vehicle["make"].lower():
                continue
            if model and model.lower() not in vehicle["model"].lower():
                continue
            if price_range:
                min_price, max_price = map(float, price_range.split('_'))
                if not min_price <= vehicle["price"] <= max_price:
                    continue
            filtered_vehicles.append(vehicle)
        
        if filtered_vehicles:
            return {"vehicle": filtered_vehicles}
        else:
            raise HTTPException(status_code=404, detail="No Vehicle found with the given parameters")
    except HTTPException as e:
        return {"error": e}
             