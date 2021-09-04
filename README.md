# SwitcherIO HomeAssistant

[PySwitcherIO](https://github.com/damob-byun/PySwitcherIO)를 이용해서 만들었습니다.

스위쳐 아이오 Switch를 홈 어시스턴트에 추가 합니다.
HACS에서 Custom Integration 추가하신담에 여기 경로 추가하세요.
블루투스 모듈이 필요합니다. 링커는 혼자 쓰고 있는데 나중에 추가 할 계획입니다.


## installation

1. HACS를 통해 설치한다. 통째로 config 안에 넣는다
2. configration.yaml을 다음과 같이 수정한다.

## How to Use

```bash
sudo hcitool lescan
```
를 통해 맥주소를 알아내고

```yaml
switch:
  - platform: switcher_io
    type: "1" #1구 2구의 경우는 2
    mac: 'XX:XX:XX:XX:XX:XX'
```

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
