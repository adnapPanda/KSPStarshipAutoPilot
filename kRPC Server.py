import krpc
conn = krpc.connect()
vessel = conn.space_center.active_vessel

flight_info = vessel.flight()

alt = conn.add_stream(getattr, flight_info, "surface_altitude")  # Starts a stream from server

refframe = vessel.surface_reference_frame
direction = conn.add_stream(vessel.direction, refframe)  # Starts a stream from server

#vessel.control.gear = False
vessel.control.sas = True
vessel.control.throttle = 1
vessel.control.activate_next_stage()
print(direction())
#vessel.control.toggle_action_group()
# 1-3 = Deactivate Engine #. 4 = Deactivate all Engines
# 5 = Activate Top Fins, 6 = Activate Bottom Fins
# Main Game Loop
#print(flight_info.angle_of_attack)

while True:
    if alt() < 2000: #  Want to keep pitch at 70
        if flight_info.pitch > 70:
            vessel.control.pitch = 0.45
        else:
            vessel.control.pitch = -0.01
        print(flight_info.pitch)
    if alt() >= 2000:
        vessel.control.toggle_action_group(1)
        if flight_info.pitch < 90:
            vessel.control.pitch = -0.45
        else:
            vessel.control.pitch = 0.01
        print(flight_info.pitch)
