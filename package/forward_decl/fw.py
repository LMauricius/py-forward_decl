import inspect
import typing

class UndeclaredReferenceError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FwDecl:
    def __init__(self) -> None:
        self.hooks: list[typing.Callable[[], None]] = []

    def add_hook(self, hook: typing.Callable[[], None]) -> None:
        self.hooks.append(hook)

    def __del__(self):
        for hook in self.hooks:
            hook()

class OpaqueFwRef:
    def __init__(self, identifier: str) -> None:
        self._iden = identifier
        self._ref = None

        # get the stack frames and their locals
        stk = inspect.stack()[1:]
        frame_dicts = [(s.frame, s.frame.f_locals) for s in stk] + [(stk[0].frame, stk[0].frame.f_globals)]

        # go up the stack until the forward-declared variable is found
        locatedref = False
        for frame, scope in frame_dicts:

            # if the frame contains the 'identifier' var
            if identifier in scope.keys():
                # check the type of the object stored in 
                fwobj = scope[identifier]
                if isinstance(fwobj, FwDecl):
                    self._saved_frame = frame
                    self._saved_scope = scope
                    def myHook():
                        self._ref = self._saved_scope[identifier]
                    fwobj.add_hook(myHook)
                else:
                    self._ref = fwobj
                locatedref = True
                break
        if not locatedref:
            raise UndeclaredReferenceError(f"Variable '{identifier}' not visible from this OpaqueFwRef.")

    def get_ref(self):
        # check if the referenced object is cached to self._ref
        if self._ref is not None:
            return self._ref
        else:
            # force update of locals() dicts
            self._saved_frame.f_locals
            self._saved_frame.f_globals

            # cache the referenced object to self._ref for faster lookup
            if not isinstance(self._saved_scope[self._iden], FwDecl):
                self._ref = self._saved_scope[self._iden]
            return self._ref
        