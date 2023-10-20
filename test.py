
@classmethod
def login():
    rfid = False
    number_of_faults = 0
    login_button_left = cls.SCREENWIDTH/5
    login_button_top = 2*cls.SCREENHEIGHT/3
    button_width = 80
    button_height = 40

    signup_button_left = 3*cls.SCREENWIDTH/5
    signup_button_top = 2*cls.SCREENHEIGHT/3

    rfid_button_left = cls.SCREENWIDTH/3
    rfid_button_top = 4*cls.SCREENHEIGHT/5

    input_rect = pygame.Rect(cls.SCREENWIDTH/3, cls.SCREENHEIGHT/2, 140, 32)
    login_button_rect = pygame.Rect(
        login_button_left, login_button_top, button_width, button_height)
    signup_button_rect = pygame.Rect(
        signup_button_left, signup_button_top, button_width, button_height)
    rfid_button_rect = pygame.Rect(
        rfid_button_left, rfid_button_top, button_width, button_height)

    clock = pygame.time.Clock()

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    active = False

    # BUTTON
    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)
    login_button_color = color_dark
    signup_button_color = color_dark
    rfid_button_color = color_dark
    smallfont = pygame.font.SysFont('Corbel', 30)
    smallerfont = pygame.font.SysFont('Corbel', 25)
    login_text = base_font.render('login', True, color)
    signup_text = smallfont.render('signup', True, color)
    rfi_text = smallfont.render('RFID', True, color)
    white = (255, 255, 255)
    red = (255, 0, 0)
    error_color = white
    error_buzz = False
    while True:
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                    if login_button_rect.collidepoint(event.pos):
                        print("login")
                        print(user_text.strip())
                        has_user, user = User.get_user_by_id(user_text)
                        if has_user:
                            return user
                        error_buzz = False
                        number_of_faults += 1
                        if number_of_faults == 3:
                            error_buzz = True
                            buzzer2.buz(1.5)
                            number_of_faults = 0
                        error_color = red
                    if signup_button_rect.collidepoint(event.pos):
                        print("signup")
                        if User.get_user_by_id(user_text)[0]:
                            return User.get_user_by_id(user_text)[1]
                        return User(user_text.strip())
                    if rfid_button_rect.collidepoint(event.pos):
                        rfid = True

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

        # it will set background color of screen
        SCREEN.fill((255, 255, 255))

        if not rfid:
            if active:
                color = color_active
            else:
                color = color_passive

            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(SCREEN, color, input_rect)
            pygame.draw.rect(SCREEN, login_button_color, login_button_rect)
            pygame.draw.rect(SCREEN, signup_button_color, signup_button_rect)
            pygame.draw.rect(SCREEN, rfid_button_color, rfid_button_rect)

            text_surface = base_font.render(user_text, True, (255, 255, 255))

            if error_buzz:
                error_text = "PAY ATTENTION!"
            else:
                error_text = f"You have failed {number_of_faults} times"
            error_text_surface = smallerfont.render(
                error_text, True, error_color)
            # print(error_text)
            # render at position stated in arguments
            SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            SCREEN.blit(login_text, (login_button_left +
                        12, login_button_top + 8))
            SCREEN.blit(signup_text, (signup_button_left +
                        12, signup_button_top + 8))
            SCREEN.blit(rfi_text, (rfid_button_left +
                        12, rfid_button_top + 8))
            SCREEN.blit(error_text_surface, (cls.SCREENWIDTH/6,  cls.SCREENHEIGHT/6))

            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width()+10)

            # display.flip() will update only a portion of the
            # screen to updated, not full area
            pygame.display.flip()

            # clock.tick(60) means that for every second at most
            # 60 frames should be passed.

            mouse = pygame.mouse.get_pos()
            if login_button_left <= mouse[0] <= login_button_left+button_width and login_button_top <= mouse[1] <= login_button_top+button_height:
                login_button_color = color_light
                # pygame.draw.rect(SCREEN, color_light, button_rect)
            else:
                login_button_color = color_dark

            if signup_button_left <= mouse[0] <= signup_button_left+button_width and signup_button_top <= mouse[1] <= signup_button_top+button_height:
                signup_button_color = color_light
                # pygame.draw.rect(SCREEN, color_light, button_rect)
            else:
                signup_button_color = color_dark

            if rfid_button_left <= mouse[0] <= rfid_button_left+button_width and rfid_button_top <= mouse[1] <= rfid_button_top+button_height:
                rfid_button_color = color_light
                # pygame.draw.rect(SCREEN, color_light, button_rect)
            else:
                rfid_button_color = color_dark
            # else:
            #     pygame.draw.rect(SCREEN, color_dark, [
            #                      cls.SCREENWIDTH/3, 2*cls.SCREENHEIGHT/3, 140, 40])
            # superimposing the text onto our button

            # updates the frames of the game
            # pygame.display.update()
            clock.tick(60)
        else:
            # pygame.image.load(cls.PLAYERS_LIST[randPlayer][0]).convert_alpha()
            text_surface = smallerfont.render(
                "Show your RFID tag.", True, (0, 0, 0))
            # print(error_text)
            # render at position stated in arguments
            SCREEN.blit(text_surface, (cls.SCREENWIDTH/4, cls.SCREENHEIGHT/2))
            pygame.display.flip()
            clock.tick(60)
            id = read_rfid()
            if User.get_user_by_id(id)[0]:
                return User.get_user_by_id(id)[1]
            return User(id)
       

@classmethod
def showWelcomeAnimation(player: User):
    """Shows welcome screen animation of flappy bird"""
    # index of player to blit on screen
    playerIndex = 0
    playerIndexGen = cycle([0, 1, 2, 1])
    # iterator used to change playerIndex after every 5th iteration
    loopIter = 0

    playerx = int(cls.SCREENWIDTH * 0.2)
    playery = int((cls.SCREENHEIGHT - cls.IMAGES['player'][0].get_height()) / 2)

    messagex = int((cls.SCREENWIDTH - cls.IMAGES['message'].get_width()) / 2)
    messagey = int(cls.SCREENHEIGHT * 0.12)

    basex = 0
    # amount by which base can maximum shift to left
    baseShift = cls.IMAGES['base'].get_width() - cls.IMAGES['background'].get_width()

    # player shm for up-down motion on welcome screen
    playerShmVals = {'val': 0, 'dir': 1}

    smallerfont = pygame.font.SysFont('Corbel', 20)
    global SOUND_DETECTED

    while True:
        if SOUND_DETECTED:
            SOUND_DETECTED=False
            cls.SOUNDS['wing'].play()
            return {
                'playery': playery + playerShmVals['val'],
                'basex': basex,
                'playerIndexGen': playerIndexGen,
            }, player
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # make first flap sound and return values for mainGame
                cls.SOUNDS['wing'].play()
                return {
                    'playery': playery + playerShmVals['val'],
                    'basex': basex,
                    'playerIndexGen': playerIndexGen,
                }, player

        # adjust playery, playerIndex, basex
        # if (loopIter + 1) % 5 == 0:
        #     playerIndex = next(playerIndexGen)
        #     print(playerIndex)
        # loopIter = (loopIter + 1) % 30
        # basex = -((-basex + 4) % baseShift)
        # playerShm(playerShmVals)

        # draw sprites
        SCREEN.blit(cls.IMAGES['background'], (0, 0))
        SCREEN.blit(cls.IMAGES['player'][playerIndex],
                    (playerx, playery + playerShmVals['val']))
        SCREEN.blit(cls.IMAGES['message'], (messagex, messagey))
        SCREEN.blit(cls.IMAGES['base'], (basex, cls.BASEY))

        text_surface = smallerfont.render(
            f"ID: {player.id}", True, (0, 0, 0))
        # print(error_text)
        # render at position stated in arguments
        SCREEN.blit(text_surface, (10, 10))
        max_score_surface = smallerfont.render(
            f"Max Score: {player.max_score}", True, (0, 0, 0))
        SCREEN.blit(max_score_surface, (cls.SCREENWIDTH - 115, 10))

        pygame.display.update()
        FPSCLOCK.tick(cls.FPS)


@classmethod
def mainGame(cls,movementInfo):
    score = playerIndex = loopIter = 0
    playerIndexGen = movementInfo['playerIndexGen']
    playerx, playery = int(cls.SCREENWIDTH * 0.2), movementInfo['playery']

    basex = movementInfo['basex']
    baseShift = cls.IMAGES['base'].get_width() - cls.IMAGES['background'].get_width()

    # get 2 new pipes to add to upperPipes lowerPipes list
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    upperPipes = [
        {'x': cls.SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': cls.SCREENWIDTH + 200 + (cls.SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]

    # list of lowerpipe
    lowerPipes = [
        {'x': cls.SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': cls.SCREENWIDTH + 200 + (cls.SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    dt = FPSCLOCK.tick(cls.FPS)/1000
    pipeVelX = -128 * dt

    # player velocity, max velocity, downward acceleration, acceleration on flap
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerMaxVelY =  10   # max vel along Y, max descend speed
    playerMinVelY =  -8   # min vel along Y, max ascend speed
    playerAccY    =   1   # players downward acceleration
    playerRot     =  45   # player's rotation
    playerVelRot  =   3   # angular speed
    playerRotThr  =  20   # rotation threshold
    playerFlapAcc =  -9   # players speed on flapping
    playerFlapped = False # True when player flaps


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > -2 * cls.IMAGES['player'][0].get_height():
                    playerVelY = playerFlapAcc
                    playerFlapped = True
                    cls.SOUNDS['wing'].play()

        # check for crash here
        crashTest = checkCrash({'x': playerx, 'y': playery, 'index': playerIndex},
                               upperPipes, lowerPipes)
        if crashTest[0]:
            return {
                'y': playery,
                'groundCrash': crashTest[1],
                'basex': basex,
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
                'playerRot': playerRot
            }

        # check for score
        playerMidPos = playerx + cls.IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + cls.IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                cls.SOUNDS['point'].play()

        # playerIndex basex change
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 100) % baseShift)

        # rotate the player
        if playerRot > -90:
            playerRot -= playerVelRot

        # player's movement
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped = False

            # more rotation to cover the threshold (calculated in visible rotation)
            playerRot = 45

        playerHeight = cls.IMAGES['player'][playerIndex].get_height()
        playery += min(playerVelY, cls.BASEY - playery - playerHeight)

        # move pipes to left
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX

        # add new pipe when first pipe is about to touch left of screen
        if 3 > len(upperPipes) > 0 and 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # remove first pipe if its out of the screen
        if len(upperPipes) > 0 and upperPipes[0]['x'] < -cls.IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # draw sprites
        SCREEN.blit(cls.IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(cls.IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(cls.IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(cls.IMAGES['base'], (basex, cls.BASEY))
        # print score so player overlaps the score
        showScore(score)

        # Player rotation has a threshold
        visibleRot = playerRotThr
        if playerRot <= playerRotThr:
            visibleRot = playerRot
        
        playerSurface = pygame.transform.rotate(cls.IMAGES['player'][playerIndex], visibleRot)
        SCREEN.blit(playerSurface, (playerx, playery))

        pygame.display.update()
        FPSCLOCK.tick(cls.FPS)

@classmethod
def showGameOverScreen(cls,crashInfo):
    """crashes the player down and shows gameover image"""
    score = crashInfo['score']
    playerx = cls.SCREENWIDTH * 0.2
    playery = crashInfo['y']
    playerHeight = cls.IMAGES['player'][0].get_height()
    playerVelY = crashInfo['playerVelY']
    playerAccY = 2
    playerRot = crashInfo['playerRot']
    playerVelRot = 7

    basex = crashInfo['basex']

    upperPipes, lowerPipes = crashInfo['upperPipes'], crashInfo['lowerPipes']

    # play hit and die cls.SOUNDS
    cls.SOUNDS['hit'].play()
    if not crashInfo['groundCrash']:
        cls.SOUNDS['die'].play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery + playerHeight >= cls.BASEY - 1:
                    return

        # player y shift
        if playery + playerHeight < cls.BASEY - 1:
            playery += min(playerVelY, cls.BASEY - playery - playerHeight)

        # player velocity change
        if playerVelY < 15:
            playerVelY += playerAccY

        # rotate only when it's a pipe crash
        if not crashInfo['groundCrash']:
            if playerRot > -90:
                playerRot -= playerVelRot

        # draw sprites
        SCREEN.blit(cls.IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(cls.IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(cls.IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(cls.IMAGES['base'], (basex, cls.BASEY))
        showScore(score)

        


        playerSurface = pygame.transform.rotate(cls.IMAGES['player'][1], playerRot)
        SCREEN.blit(playerSurface, (playerx,playery))
        SCREEN.blit(cls.IMAGES['gameover'], (50, 180))

        FPSCLOCK.tick(cls.FPS)
        pygame.display.update()


def playerShm(playerShm):
    """oscillates the value of playerShm['val'] between 8 and -8"""
    if abs(playerShm['val']) == 8:
        playerShm['dir'] *= -1

    if playerShm['dir'] == 1:
         playerShm['val'] += 1
    else:
        playerShm['val'] -= 1


def getRandomPipe():
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    gapY = random.randrange(0, int(cls.BASEY * 0.6 - cls.PIPEGAPSIZE))
    gapY += int(cls.BASEY * 0.2)
    pipeHeight = cls.IMAGES['pipe'][0].get_height()
    pipeX = cls.SCREENWIDTH + 10

    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + cls.PIPEGAPSIZE}, # lower pipe
    ]


def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += cls.IMAGES['numbers'][digit].get_width()

    Xoffset = (cls.SCREENWIDTH - totalWidth) / 2

    for digit in scoreDigits:
        SCREEN.blit(cls.IMAGES['numbers'][digit], (Xoffset, cls.SCREENHEIGHT * 0.1))
        Xoffset += cls.IMAGES['numbers'][digit].get_width()


def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collides with base or pipes."""
    pi = player['index']
    player['w'] = cls.IMAGES['player'][0].get_width()
    player['h'] = cls.IMAGES['player'][0].get_height()

    # if player crashes into ground
    if player['y'] + player['h'] >= cls.BASEY - 1:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        pipeW = cls.IMAGES['pipe'][0].get_width()
        pipeH = cls.IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe cls.HITMASKS
            pHitMask = cls.HITMASKS['player'][pi]
            uHitmask = cls.HITMASKS['pipe'][0]
            lHitmask = cls.HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)

            if uCollide or lCollide:
                return [True, False]

    return [False, False]

def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """Checks if two objects collide and not just their rects"""
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False

def getHitmask(image):
    """returns a hitmask using an image's alpha."""
    mask = []
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask