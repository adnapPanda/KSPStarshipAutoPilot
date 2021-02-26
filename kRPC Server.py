import krpc
conn = krpc.connect()
vessel = conn.space_center.active_vessel

flight_info = vessel.flight()

#refframe = vessel.flight
alt = conn.add_stream(getattr, flight_info, "surface_altitude")

vessel.control.sas = True
vessel.control.throttle = 1
vessel.control.activate_next_stage()

# Main Game Loop
while True:
    if alt() >= 10000:
        vessel.control.throttle = 0

