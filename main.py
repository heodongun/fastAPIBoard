from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 모델 정의 (기존 코드와 동일)
class AuthSignInRequest(BaseModel):
    email: str
    password: str

class AuthSignInResponse(BaseModel):
    code: str
    message: str
    token: str
    expirationTime: int

class AuthSignUpRequest(BaseModel):
    email: str
    password: str
    nickname: str
    telNumber: str
    address: str
    addressDetail: Optional[str] = None
    agreedPersonal: bool

class AuthSignUpResponse(BaseModel):
    code: str
    message: str

class BoardListItem(BaseModel):
    boardNumber: int
    title: str
    content: str
    boardTitleImage: Optional[str] = None
    favoriteCount: int
    commentCount: int
    viewCount: int
    writeDatetime: str
    writerNickname: str
    writerProfileImage: Optional[str] = None

class LatestBoardListResponse(BaseModel):
    code: str
    message: str
    latestList: List[BoardListItem]

class Top3BoardListResponse(BaseModel):
    code: str
    message: str
    top3List: List[BoardListItem]

class SearchBoardListResponse(BaseModel):
    code: str
    message: str
    searchList: List[BoardListItem]

class UserBoardListResponse(BaseModel):
    code: str
    message: str
    userBoardList: List[BoardListItem]

class BoardDetailResponse(BaseModel):
    code: str
    message: str
    boardNumber: int
    title: str
    content: str
    boardImageList: List[str]
    writeDatetime: str
    writerEmail: str
    writerNickname: str
    writerProfileImage: Optional[str] = None

class FavoriteListItem(BaseModel):
    email: str
    nickname: str
    profileImage: Optional[str] = None

class FavoriteListResponse(BaseModel):
    code: str
    message: str
    favoriteList: List[FavoriteListItem]

class CommentListItem(BaseModel):
    nickname: str
    profileImage: Optional[str] = None
    writeDatetime: str
    content: str

class CommentListResponse(BaseModel):
    code: str
    message: str
    commentList: List[CommentListItem]

class BoardWriteRequest(BaseModel):
    title: str
    content: str
    boardImageList: List[str]

class BoardWriteResponse(BaseModel):
    code: str
    message: str

class CommentWriteRequest(BaseModel):
    content: str

class CommentWriteResponse(BaseModel):
    code: str
    message: str

class BoardUpdateRequest(BaseModel):
    title: str
    content: str
    boardImageList: List[str]

class BoardUpdateResponse(BaseModel):
    code: str
    message: str

class FavoriteResponse(BaseModel):
    code: str
    message: str

class BoardDeleteResponse(BaseModel):
    code: str
    message: str

class PopularWordListResponse(BaseModel):
    code: str
    message: str
    popularWordList: List[str]

class RelativeWordListResponse(BaseModel):
    code: str
    message: str
    relativeWordList: List[str]

class UserInfoResponse(BaseModel):
    code: str
    message: str
    email: str
    nickname: str
    profileImage: Optional[str] = None

class UserNicknameUpdateRequest(BaseModel):
    nickname: str

class UserNicknameUpdateResponse(BaseModel):
    code: str
    message: str

class UserProfileImageUpdateRequest(BaseModel):
    profileImage: Optional[str] = None

class UserProfileImageUpdateResponse(BaseModel):
    code: str
    message: str

# 임시 데이터 저장소 (메모리)
boards = [
    BoardListItem(boardNumber=1, title="오늘 점심 뭐먹지...", content="오늘 점심...", boardTitleImage=None, favoriteCount=0, commentCount=0, viewCount=0, writeDatetime="2023.08.18. 00:54:27", writerNickname="주코야키", writerProfileImage=None),
    BoardListItem(boardNumber=2, title="이번 주 인기 게시글", content="인기...", boardTitleImage=None, favoriteCount=10, commentCount=5, viewCount=100, writeDatetime="2023.08.17. 10:00:00", writerNickname="인기쟁이", writerProfileImage=None),
    BoardListItem(boardNumber=3, title="두 번째 인기 게시글", content="인기...", boardTitleImage=None, favoriteCount=8, commentCount=3, viewCount=80, writeDatetime="2023.08.16. 15:30:00", writerNickname="나도인기", writerProfileImage=None),
    BoardListItem(boardNumber=4, title="세 번째 인기 게시글", content="인기...", boardTitleImage=None, favoriteCount=5, commentCount=2, viewCount=60, writeDatetime="2023.08.15. 20:00:00", writerNickname="곧인기", writerProfileImage=None),
    BoardListItem(boardNumber=5, title="검색 결과 1", content="검색...", boardTitleImage=None, favoriteCount=1, commentCount=0, viewCount=10, writeDatetime="2023.08.19. 09:00:00", writerNickname="검색왕", writerProfileImage=None),
    BoardListItem(boardNumber=6, title="유저 게시글 1", content="유저...", boardTitleImage=None, favoriteCount=2, commentCount=1, viewCount=20, writeDatetime="2023.08.20. 14:00:00", writerNickname="테스트유저", writerProfileImage=None)
]
comments = [
    CommentListItem(nickname="댓글1", profileImage=None, writeDatetime="2023.08.22. 09:30:00", content="첫 번째 댓글"),
    CommentListItem(nickname="댓글2", profileImage=None, writeDatetime="2023.08.22. 10:00:00", content="두 번째 댓글")
]
popular_words_list = ["아침", "점심", "저녁"]
relative_words_list = ["오늘", "내일", "모레"]
users = {
    "test@email.com": UserInfoResponse(code="SU", message="Success.", email="test@email.com", nickname="테스트닉네임", profileImage=None)
}

# FastAPI 앱 생성 (기존 코드와 동일)
app = FastAPI()

# CORS 미들웨어 설정 (기존 코드와 동일)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth 라우터 (기존 코드와 동일)
@app.post("/api/v1/auth/sign-in", response_model=AuthSignInResponse)
async def sign_in(request: AuthSignInRequest):
    if request.email == "email@email.com" and request.password == "P!ssw0rd":
        return AuthSignInResponse(code="SU", message="Success.", token="임시토큰", expirationTime=3600)
    else:
        raise HTTPException(status_code=401, detail={"code": "SF", "message": "Login information mismatch."})

@app.post("/api/v1/auth/sign-up", response_model=AuthSignUpResponse)
async def sign_up(request: AuthSignUpRequest):
    if request.email in users:
        raise HTTPException(status_code=400, detail={"code": "DE", "message": "Duplicate email."})
    users[request.email] = UserInfoResponse(code="SU", message="Success.", email=request.email, nickname=request.nickname, profileImage=None)
    return AuthSignUpResponse(code="SU", message="Success.")

# Board 라우터
@app.get("/api/v1/board/latest-list", response_model=LatestBoardListResponse)
async def get_latest_list():
    return LatestBoardListResponse(code="SU", message="Success.", latestList=boards[-5:]) # 최근 5개 게시물

@app.get("/api/v1/board/top-3", response_model=Top3BoardListResponse)
async def get_top3_list():
    return Top3BoardListResponse(code="SU", message="Success.", top3List=sorted(boards, key=lambda x: x.favoriteCount + x.commentCount + x.viewCount, reverse=True)[:3])

@app.get("/api/v1/board/search-list/{searchWord}", response_model=SearchBoardListResponse)
async def get_search_list(searchWord: str):
    results = [board for board in boards if searchWord in board.title or searchWord in board.content]
    return SearchBoardListResponse(code="SU", message="Success.", searchList=results)

@app.get("/api/v1/board/search-list/{searchWord}/{preSearchWord}", response_model=SearchBoardListResponse)
async def get_search_list_with_prev(searchWord: str, preSearchWord: str):
    results = [board for board in boards if searchWord in board.title or searchWord in board.content or preSearchWord in board.title or preSearchWord in board.content]
    return SearchBoardListResponse(code="SU", message="Success.", searchList=results)

@app.get("/api/v1/board/user-board-list/{email}", response_model=UserBoardListResponse)
async def get_user_board_list(email: str):
    user_boards_list = [board for board in boards if board_detail.writerEmail == email] # 임시로 board_detail의 작성자 이메일 사용
    if user_boards_list:
        return UserBoardListResponse(code="SU", message="Success.", userBoardList=user_boards_list)
    else:
        raise HTTPException(status_code=400, detail={"code": "NU", "message": "This user does not exist."})

@app.get("/api/v1/board/{boardNumber}", response_model=BoardDetailResponse)
async def get_board_detail(boardNumber: int):
    for board in boards:
        if board.boardNumber == boardNumber:
            return BoardDetailResponse(code="SU", message="Success.", boardNumber=board.boardNumber, title=board.title, content=board.content, boardImageList=[], writeDatetime=board.writeDatetime, writerEmail="test@email.com", writerNickname=board.writerNickname, writerProfileImage=board.writerProfileImage)
    raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.get("/api/v1/board/{boardNumber}/favorite-list", response_model=FavoriteListResponse)
async def get_favorite_list(boardNumber: int):
    # 실제 서비스에서는 게시물 ID에 따른 좋아요 목록 관리 필요
    if boardNumber > 0:
        return FavoriteListResponse(code="SU", message="Success.", favoriteList=favorite_list)
    else:
        raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.get("/api/v1/board/{boardNumber}/comment-list", response_model=CommentListResponse)
async def get_comment_list(boardNumber: int):
    # 실제 서비스에서는 게시물 ID에 따른 댓글 목록 관리 필요
    if boardNumber > 0:
        return CommentListResponse(code="SU", message="Success.", commentList=comments)
    else:
        raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.post("/api/v1/board", response_model=BoardWriteResponse)
async def write_board(request: BoardWriteRequest):
    new_board_number = len(boards) + 1
    new_board = BoardListItem(boardNumber=new_board_number, title=request.title, content=request.content, boardTitleImage=None, favoriteCount=0, commentCount=0, viewCount=0, writeDatetime="현재 시간", writerNickname="로그인유저", writerProfileImage=None) # 실제로는 현재 시간 및 로그인 유저 정보 사용
    boards.append(new_board)
    return BoardWriteResponse(code="SU", message="Success.")

@app.post("/api/v1/board/{boardNumber}/comment", response_model=CommentWriteResponse)
async def write_comment(boardNumber: int, request: CommentWriteRequest):
    if boardNumber > 0:
        new_comment = CommentListItem(nickname="로그인유저", profileImage=None, writeDatetime="현재 시간", content=request.content) # 실제로는 현재 시간 및 로그인 유저 정보 사용
        comments.append(new_comment)
        return CommentWriteResponse(code="SU", message="Success.")
    else:
        raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.patch("/api/v1/board/{boardNumber}", response_model=BoardUpdateResponse)
async def update_board(boardNumber: int, request: BoardUpdateRequest):
    for board in boards:
        if board.boardNumber == boardNumber:
            board.title = request.title
            board.content = request.content
            board.boardImageList = request.boardImageList
            return BoardUpdateResponse(code="SU", message="Success.")
    raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.put("/api/v1/board/{boardNumber}/favorite", response_model=FavoriteResponse)
async def favorite_board(boardNumber: int):
    for board in boards:
        if board.boardNumber == boardNumber:
            board.favoriteCount += 1
            return FavoriteResponse(code="SU", message="Success.")
    raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

@app.delete("/api/v1/board/{boardNumber}", response_model=BoardDeleteResponse)
async def delete_board(boardNumber: int):
    global boards
    initial_len = len(boards)
    boards = [board for board in boards if board.boardNumber != boardNumber]
    if len(boards) < initial_len:
        return BoardDeleteResponse(code="SU", message="Success.")
    else:
        raise HTTPException(status_code=400, detail={"code": "NB", "message": "This board does not exist."})

# Search 라우터 (기존 코드와 동일)
@app.get("/api/v1/search/popular-list", response_model=PopularWordListResponse)
async def get_popular_list():
    return PopularWordListResponse(code="SU", message="Success.", popularWordList=popular_words_list)

@app.get("/api/v1/search/{searchWord}/relation-list", response_model=RelativeWordListResponse)
async def get_relation_list(searchWord: str):
    return RelativeWordListResponse(code="SU", message="Success.", relativeWordList=relative_words_list)

@app.get("/api/v1/user/{email}", response_model=UserInfoResponse)
async def get_user_info(email: str):
    if email in users:
        return users[email]
    else:
        raise HTTPException(status_code=400, detail={"code": "NU", "message": "This user does not exist."})

@app.get("/api/v1/user", response_model=UserInfoResponse)
async def get_logged_in_user_info():
    # 실제 서비스에서는 인증 정보 확인 필요
    # 임시로 첫 번째 유저 정보를 반환
    if users:
        return list(users.values())[0]
    else:
        raise HTTPException(status_code=401, detail={"code": "NU", "message": "This user does not exist."})

@app.patch("/api/v1/user/nickname", response_model=UserNicknameUpdateResponse)
async def update_nickname(request: UserNicknameUpdateRequest):
    # 실제 서비스에서는 인증 정보 확인 및 데이터베이스 업데이트 로직 필요
    if len(request.nickname) > 2:
        # 임시로 첫 번째 유저의 닉네임 업데이트
        if users:
            first_user_email = list(users.keys())[0]
            users[first_user_email].nickname = request.nickname
            return UserNicknameUpdateResponse(code="SU", message="Success.")
        else:
            raise HTTPException(status_code=401, detail={"code": "NU", "message": "This user does not exist."})
    else:
        raise HTTPException(status_code=400, detail={"code": "VF", "message": "Validation failed."})

@app.patch("/api/v1/user/profile-image", response_model=UserProfileImageUpdateResponse)
async def update_profile_image(request: UserProfileImageUpdateRequest):
    # 실제 서비스에서는 인증 정보 확인 및 데이터베이스 업데이트 로직 필요
    # 임시로 첫 번째 유저의 프로필 이미지 업데이트
    if users:
        first_user_email = list(users.keys())[0]
        users[first_user_email].profileImage = request.profileImage
        return UserProfileImageUpdateResponse(code="SU", message="Success.")
    else:
        raise HTTPException(status_code=401, detail={"code": "NU", "message": "This user does not exist."})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)