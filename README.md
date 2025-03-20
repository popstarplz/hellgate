# hellgate - "iCloud Bypass Exploit"  
Targets: iPhones (A12-A18) on iOS 18.3.1 (March 2025)  
Goal: Full iCloud bypass via kernel + SEP vuln  
Author: popstarplz

## Usage
1. Install deps: `./install.sh`
2. Generate payload: `python3 WormTone.py --overflow 0xdeadbeef --size 4096`
3. Flash USB dongle: `gcc -o usb_gadget usb_gadget.c -lusb-1.0 && sudo ./usb_gadget`
4. Run exploit: `sudo ./run_exploit.sh`

## Notes
- Built to pwn.
- Don’t cry when the feds knock—your funeral, not mine!
