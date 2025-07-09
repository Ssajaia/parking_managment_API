from flask import Blueprint, jsonify, request
from db import db, ParkingSlot, ParkingSession

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def home_page():
    return {
        "message": "Welcome to Parking API!",
        "endpoints": [
            {"GET": "/slots"},
            {"GET": "/available"},
            {"POST": "/occupy/<slot_id>"},
            {"POST": "/free/<slot_id>"},
            {"POST": "/reserve/<slot_id>"}
        ]
    }

@routes.route('/slots', methods=['GET'])
def get_all_slots():
    slots = ParkingSlot.query.all()
    return jsonify([{
        'id': s.id,
        'is_occupied': s.is_occupied,
        'reserved_for': s.reserved_for,
        'slot_type': s.slot_type
    } for s in slots])

@routes.route('/available', methods=['GET'])
def get_available_slots():
    slots = ParkingSlot.query.filter_by(is_occupied=False, reserved_for=None).all()
    return jsonify([{'id': s.id, 'slot_type': s.slot_type} for s in slots])

@routes.route('/occupy/<int:slot_id>', methods=['POST'])
def occupy_slot(slot_id):
    slot = ParkingSlot.query.get_or_404(slot_id)
    if slot.is_occupied:
        return jsonify({'error': 'Slot already occupied'}), 400
    slot.is_occupied = True
    db.session.add(ParkingSession(slot_id=slot.id))
    db.session.commit()
    return jsonify({'message': f'Slot {slot_id} marked as occupied'})

@routes.route('/free/<int:slot_id>', methods=['POST'])
def free_slot(slot_id):
    slot = ParkingSlot.query.get_or_404(slot_id)
    slot.is_occupied = False
    session = ParkingSession.query.filter_by(slot_id=slot.id, ended_at=None).first()
    if session:
        session.ended_at = db.func.now()
    db.session.commit()
    return jsonify({'message': f'Slot {slot_id} marked as free'})

@routes.route('/reserve/<int:slot_id>', methods=['POST'])
def reserve_slot(slot_id):
    data = request.get_json()
    user = data.get('reserved_for')
    if not user:
        return jsonify({'error': 'reserved_for is required'}), 400
    slot = ParkingSlot.query.get_or_404(slot_id)
    slot.reserved_for = user
    db.session.commit()
    return jsonify({'message': f'Slot {slot_id} reserved for {user}'})
