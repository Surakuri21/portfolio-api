import httpx
from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Gag AI Assistant"])


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    gag_script: list[str]


@router.post("/", response_model=ChatResponse)
async def fake_ai_response(request: Request, payload: ChatRequest):
    """
    Simulates an AI response but returns a highly specific network fingerprinting gag script.
    """
    # 1. Extract the user's IP address
    forwarded_for = request.headers.get("x-forwarded-for")
    client_ip = forwarded_for.split(",")[0] if forwarded_for else request.client.host

    # 2. Look up ISP and Location via ip-api.com
    # Default fallback data just in case the API fails or is rate-limited
    location_data = {
        "city": "Unknown City",
        "regionName": "Unknown Region",
        "country": "Unknown Country",
        "isp": "Unknown ISP",
        "timezone": "Unknown Timezone",
        "lat": 0.0,
        "lon": 0.0,
    }

    if client_ip not in ["127.0.0.1", "localhost", "::1"]:
        try:
            async with httpx.AsyncClient() as client:
                res = await client.get(
                    f"http://ip-api.com/json/{client_ip}", timeout=3.0
                )
                if res.status_code == 200:
                    data = res.json()
                    location_data = {
                        "city": data.get("city", "Unknown City"),
                        "regionName": data.get("regionName", "Unknown Region"),
                        "country": data.get("country", "Unknown Country"),
                        "isp": data.get("isp", "Unknown ISP"),
                        "timezone": data.get("timezone", "Unknown Timezone"),
                        "lat": data.get("lat", 0.0),
                        "lon": data.get("lon", 0.0),
                    }
        except Exception:
            pass

    # 3. Formulate the exact script
    # Note: [OS], [CORES], [RAM], [BROWSER], [LANG], and [TIME] are placeholders.
    # Our React frontend will dynamically replace these before animating the text.
    script = [
        "Thinking...",
        "Analyzing...",
        "before i answer",
        "Here is what your browser already shared the moment you opened this site",
        f"your public ip address is {client_ip}",
        f"you are connected through {location_data['isp']}",
        f"your approximate coordinates are around {location_data['lat']}, {location_data['lon']}",
        f"you are currently in {location_data['city']}, {location_data['regionName']}, {location_data['country']}",
        "you are on a [OS] device with [CORES] processor cores and [RAM]gb of memory",
        "you are browsing with [BROWSER] set to [LANG]",
        f"your timezone is {location_data['timezone']} and it is around [TIME] where you are",
        "none of this needed your permission",
        "your browser shares it with every website you open, automatically",
        "so be mindful of what you click, and who you trust online",
        "as for your question",
        "i don't want to waste tokens on that, search for it yourself :)",
    ]

    return ChatResponse(gag_script=script)
