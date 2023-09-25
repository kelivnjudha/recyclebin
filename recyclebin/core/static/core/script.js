alert('JavaScript is running');

let isDragging = false;
let initialX;
let deltaX = 0;
const threshold = 50; // Adjust this threshold as needed

const cards = document.querySelectorAll('.card');

cards.forEach((card) => {
  card.addEventListener('mousedown', handleDragStart);
  card.addEventListener('touchstart', handleDragStart, { passive: true });
  card.addEventListener('mousemove', handleDrag);
  card.addEventListener('touchmove', handleDrag, { passive: true });
  card.addEventListener('mouseup', handleDragEnd);
  card.addEventListener('touchend', handleDragEnd);
});

function handleDragStart(event) {
  isDragging = true;
  initialX = event.clientX || event.touches[0].clientX;
}

function handleDrag(event) {
  if (!isDragging) return;

  const currentX = event.clientX || event.touches[0].clientX;
  deltaX = currentX - initialX;
}

function handleDragEnd() {
  if (isDragging) {
    isDragging = false;

    if (deltaX > threshold) {
      swipe('left');
    } else if (deltaX < -threshold) {
      swipe('right');
    }

    deltaX = 0;
  }
}

function swipe(direction) {
  console.log('swipe', direction);

  cards.forEach((card) => {
    const classes = card.classList;
    let positionClass = '';

    // Find the class that starts with 'position'
    for (const className of classes) {
      if (className.startsWith('position')) {
        positionClass = className;
        break;
      }
    }

    const positionNumber = parseInt(positionClass.slice(-1));

    let newPositionNumber;
    if (direction === 'left') {
      newPositionNumber = positionNumber === 0 ? 7 : positionNumber - 1;
    } else if (direction === 'right') {
      newPositionNumber = positionNumber === 7 ? 0 : positionNumber + 1;
    }

    // Remove the current position class and add the new one
    classes.remove(positionClass);
    classes.add(`position${newPositionNumber}`);
  });
}
