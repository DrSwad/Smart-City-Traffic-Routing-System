import requests

BASE_URL = "http://localhost:8000/api/v1/traffic"


def create_sample_intersections():
    intersections = [
        {
            "name": "Gulshan-1 Circle",
            "latitude": 23.7937,
            "longitude": 90.4066,
            "description": "Major intersection connecting Gulshan-1 and Banani",
        },
        {
            "name": "Farmgate",
            "latitude": 23.7467,
            "longitude": 90.3847,
            "description": "Busy intersection near Dhaka University",
        },
        {
            "name": "Kakrail",
            "latitude": 23.7289,
            "longitude": 90.3944,
            "description": "Central Dhaka intersection near Ramna Park",
        },
        {
            "name": "Mohammadpur",
            "latitude": 23.7639,
            "longitude": 90.3589,
            "description": "Residential area intersection",
        },
        {
            "name": "Dhanmondi-27",
            "latitude": 23.7467,
            "longitude": 90.3656,
            "description": "Popular area near Dhanmondi Lake",
        },
    ]

    created_intersections = []
    for intersection in intersections:
        response = requests.post(f"{BASE_URL}/intersections", json=intersection)
        if response.status_code == 200:
            created_intersections.append(response.json())
            print(f"Created intersection: {intersection['name']}")

    return created_intersections


def main():
    print("Creating sample intersections...")
    intersections = create_sample_intersections()

    print("\nSample data creation completed!")
    print(f"Created {len(intersections)} intersections")


if __name__ == "__main__":
    main()
