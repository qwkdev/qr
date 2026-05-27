#!/usr/bin/env bash

set -e

INSTALL="$HOME/.local/bin"
TARGET="$INSTALL/qr"
FILES="$HOME/.local/share/qr"

mkdir -p "$FILES"
cp "main.py" "$FILES"

echo "Creating venv..."
python3 -m venv "$FILES/venv"
"$FILES/venv/bin/pip" install pillow qrcode

mkdir -p "$INSTALL"

cat > "$TARGET" <<EOF
#!/usr/bin/env bash
exec "$FILES/venv/bin/python" "$FILES/main.py" "\$@"
EOF

chmod +x "$TARGET"

if ! echo "$PATH" | grep -q "$INSTALL"; then
    echo ""
    echo "WARNING: $INSTALL is not in your PATH."
    echo "Add this to your shell config:"
    echo 'export PATH="$HOME/.local/bin:$PATH"'
fi

echo "Done"