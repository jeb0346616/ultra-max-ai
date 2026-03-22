name: Build APK

on:
  workflow_dispatch:
  push:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y openjdk-17-jdk zip unzip git
        pip install --upgrade pip
        pip install buildozer cython

    - name: Build APK
      run: |
        buildozer init || true
        buildozer -v android debug || true

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apk
