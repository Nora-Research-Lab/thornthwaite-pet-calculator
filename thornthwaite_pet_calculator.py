import math

def heat_index(T):
    """Monthly heat index i = (T/5)**1.514 if T>0 else 0."""
    if T > 0:
        return (T / 5.0) ** 1.514
    return 0.0

def annual_heat_index(monthly_temps):
    """Compute annual heat index I = sum of monthly heat indices."""
    return sum(heat_index(t) for t in monthly_temps)

def alpha(I):
    """Thornthwaite exponent a = 6.75e-7 I^3 - 7.71e-5 I^2 + 1.792e-2 I + 0.49239."""
    return (6.75e-7 * I**3 - 7.71e-5 * I**2 + 1.792e-2 * I + 0.49239)

def unadjusted_pet(T, I, a):
    """Unadjusted monthly PET (mm/month) = 16 * (10*T/I)**a if T>0 else 0."""
    if T <= 0:
        return 0.0
    return 16.0 * ((10.0 * T / I) ** a)

def day_length_n(lat_rad, declination_rad):
    """Day length in hours from latitude and solar declination (both in radians)."""
    cos_hour_angle = -math.tan(lat_rad) * math.tan(declination_rad)
    # Clamp to [-1,1] to avoid domain errors at high latitudes
    cos_hour_angle = max(-1.0, min(1.0, cos_hour_angle))
    hour_angle = math.acos(cos_hour_angle)
    return (24.0 / math.pi) * hour_angle

def solar_declination(day_of_year):
    """Solar declination in radians for a given day of year (1-365)."""
    # Approximation for the 15th of each month
    angle = 2.0 * math.pi / 365.0 * (284.0 + day_of_year)
    return math.radians(23.45 * math.sin(angle))

# Days in month (non-leap)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Day of year for the 15th of each month
day_of_year_15th = [15, 46, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349]

def monthly_pet(temperatures, latitude_signed):
    """
    Calculate Thornthwaite PET for 12 months.
    temperatures: list of 12 monthly mean temperatures (°C)
    latitude_signed: latitude in degrees, positive for Northern, negative for Southern
    Returns: (list of 12 corrected PET values in mm/month, annual total in mm)
    """
    if len(temperatures) != 12:
        raise ValueError("Exactly 12 monthly temperatures required.")
    I = annual_heat_index(temperatures)
    if I == 0:
        # All temperatures <= 0 → no PET
        return [0.0] * 12, 0.0
    a = alpha(I)
    lat_rad = math.radians(latitude_signed)
    corrected_pets = []
    for i in range(12):
        t = temperatures[i]
        unadj = unadjusted_pet(t, I, a)
        if unadj == 0.0:
            corrected_pets.append(0.0)
            continue
        doy = day_of_year_15th[i]
        decl = solar_declination(doy)
        N = day_length_n(lat_rad, decl)
        adj_factor = (N / 12.0) * (days_in_month[i] / 30.0)
        corrected_pets.append(unadj * adj_factor)
    annual = sum(corrected_pets)
    return corrected_pets, annual
